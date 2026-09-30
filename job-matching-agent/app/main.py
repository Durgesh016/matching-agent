import requests

from app.agents.job_agent import JobAgent
from app.agents.job_search_agent import JobSearchAgent
from app.agents.matching_agent import MatchingAgent
from app.agents.ai_match_agent import AIMatchAgent

from app.services.report_service import create_job_report
from app.services.adzuna_job_source import AdzunaJobSource, resolve_country
from app.services.job_skill_extractor import JobSkillExtractor
from app.services.text_cleaner import clean_html
from app.services.experience_extractor import ExperienceExtractor


def ask_country() -> str:

    while True:

        value = input(
            "Enter country (US / India / UK / Canada / Australia ..., "
            "or press Enter for US): "
        ).strip()

        if not value:
            return "us"

        country = resolve_country(value)

        if country:
            return country

        print(
            "Adzuna doesn't support that country. Supported: US, India, UK, "
            "Canada, Australia, New Zealand, Singapore, South Africa, Germany, "
            "France, Netherlands, Italy, Spain, Austria, Belgium, Switzerland, "
            "Poland, Brazil, Mexico."
        )


def main():

    # =========================================
    # PATHS
    # =========================================

    pdf_path = "data/resumes/Roles & Skills.pdf"
    common_skills_path = "data/skills/common_skills.txt"
    output_path = "output/job_match_report.docx"

    # =========================================
    # INITIALIZE AGENTS / SERVICES
    # =========================================

    job_agent = JobAgent()
    search_agent = JobSearchAgent()
    matching_agent = MatchingAgent()
    ai_agent = AIMatchAgent()
    skill_extractor = JobSkillExtractor()
    experience_extractor = ExperienceExtractor()

    # =========================================
    # LOAD SKILLS PDF
    # =========================================

    pdf_text = job_agent.read_jobs_pdf(pdf_path)

    available_jobs = job_agent.extract_jobs(pdf_text)

    print(f"Skills dataset loaded: " f"{len(available_jobs)} roles")

    pdf_skills = skill_extractor.extract_skills_from_pdf_roles(available_jobs)

    # Search job descriptions for the PDF skills AND common
    # skills, so skills the PDF doesn't have can be found
    # and reported as missing.
    skill_vocabulary = skill_extractor.build_vocabulary(
        skill_extractor.load_skill_file(common_skills_path), pdf_skills
    )

    print(
        f"Skill vocabulary loaded: {len(pdf_skills)} PDF skills, "
        f"{len(skill_vocabulary)} searchable skills"
    )

    # =========================================
    # JOB SEARCH
    # =========================================

    print("\n========== JOB SEARCH ==========")

    role = input("Enter role: ").strip()

    country = ask_country()

    location = input(
        "Enter city/state (or press Enter for the whole country): "
    ).strip()

    # A country typed as the location, e.g. "India"
    location_country = resolve_country(location, allow_codes=False)

    if location_country:

        country = location_country

        location = ""

    # =========================================
    # LOAD JOBS FROM ADZUNA
    # =========================================

    try:

        job_source = AdzunaJobSource(country=country)

        jobs = job_source.get_jobs(role=role, location=location)

    except ValueError as error:

        print(f"\n{error}")

        return

    except requests.HTTPError as error:

        # The full error text contains the request URL
        # with your API keys, so only show the status.
        print(f"\nAdzuna returned an error: HTTP {error.response.status_code}")

        return

    except requests.RequestException as error:

        print(
            f"\nCould not reach Adzuna ({type(error).__name__}). "
            "Check your internet connection."
        )

        return

    print(f"\nJobs loaded from Adzuna: " f"{len(jobs)}")

    if not jobs:

        print("No jobs found.")

        return

    # =========================================
    # CLEAN DESCRIPTIONS / EXTRACT EXPERIENCE
    # =========================================

    print("\nExtracting experience requirements...")

    for job in jobs:

        job.description = clean_html(job.description or "")

        job.experience = experience_extractor.extract(job.description, job.title)

    # =========================================
    # USER FILTERS
    # =========================================

    experience = input(
        "\nEnter experience "
        "(Internship / Entry Level / "
        "0-1 years / 1-3 years / "
        "3-5 years / 5+ years, "
        "or press Enter for all): "
    ).strip()

    if experience and not search_agent.normalize_experience(experience):

        print("Unknown experience level, showing all levels.")

    posted_within = input(
        "Posted within " "(24 hours / 3 days / 7 days / " "14 days, or Enter for all): "
    ).strip()

    # =========================================
    # APPLY ALL FILTERS
    # =========================================

    filtered_jobs = search_agent.search(
        jobs,
        role=role or None,
        location=location or None,
        experience=experience or None,
        posted_within=posted_within or None,
    )

    print(f"\nJobs after filters: " f"{len(filtered_jobs)}")

    if experience:

        print("(Jobs that don't mention experience are kept.)")

    if not filtered_jobs:

        print("No jobs matched your filters.")

        return

    # =========================================
    # PROCESS JOBS
    # =========================================

    results = []

    for job in filtered_jobs:

        experience_label = job.experience or "Not specified"

        print("\n--------------------------------")

        print("Job       :", job.title)

        print("Company   :", job.company)

        print("Location  :", job.location)

        print("Experience:", experience_label)

        print("Posted    :", job.posted_date)

        # =====================================
        # EXTRACT SKILLS
        # =====================================

        job.skills = skill_extractor.extract(job.description, skill_vocabulary)

        print("Skills    :", job.skills)

        # =====================================
        # MATCH WITH PDF
        # =====================================

        result = matching_agent.calculate_match(job, available_jobs)

        print("Match     :", result["match_percentage"], "%")

        print("Matched   :", result["matched_skills"])

        print("Missing   :", result["missing_skills"])

        print("PDF Roles :", result["relevant_roles"])

        # =====================================
        # AI ANALYSIS
        # =====================================

        print("\nRunning AI analysis...")

        analysis = ai_agent.analyze(
            job_title=job.title,
            company=job.company,
            job_skills=job.skills,
            matched_skills=(result["matched_skills"]),
            missing_skills=(result["missing_skills"]),
        )

        print("\nAI Analysis:")

        print(analysis)

        # =====================================
        # STORE RESULT
        # =====================================

        results.append(
            {
                "job_title": job.title,
                "company": job.company,
                "location": job.location,
                "experience": experience_label,
                "source_url": job.source_url,
                "match_percentage": result["match_percentage"],
                "matched_skills": result["matched_skills"],
                "missing_skills": result["missing_skills"],
                "relevant_roles": result["relevant_roles"],
                "analysis": analysis,
            }
        )

    # =========================================
    # GENERATE REPORT
    # =========================================

    print("\nGenerating report...")

    saved_path = create_job_report(results, output_path)

    print("\n================================")

    print("Report generated successfully!")

    print("File:", saved_path)


if __name__ == "__main__":
    main()
