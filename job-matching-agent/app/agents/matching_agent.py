import re

from app.models.schemas import JobPosting
from app.services.skill_matcher import is_skill_covered, normalize_skills

# Words ignored when comparing a job title with PDF role names
TITLE_STOPWORDS = {"and", "or", "of", "the", "a", "an", "to", "in", "for", "i", "ii", "iii"}


class MatchingAgent:

    def calculate_match(
        self,
        job: JobPosting,
        available_jobs
    ):
        # All skills from the PDF (your skill profile)
        pdf_skills = set()

        for role in available_jobs:
            pdf_skills |= normalize_skills(role.skills)

        # Skills explicitly found in the job description
        job_skills = normalize_skills(job.skills)

        matched_skills = {
            skill for skill in job_skills
            if is_skill_covered(skill, pdf_skills)
        }
        missing_skills = job_skills - matched_skills

        if job_skills:
            match_percentage = (
                len(matched_skills)
                / len(job_skills)
            ) * 100
        else:
            match_percentage = 0

        return {
            "job_title": job.title,
            "company": job.company,
            "match_percentage": round(match_percentage, 2),
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills),
            "relevant_roles": self._relevant_roles(job, matched_skills, available_jobs)
        }

    def _relevant_roles(self, job: JobPosting, matched_skills: set[str], available_jobs, limit: int = 3) -> list[str]:
        """
        PDF roles most similar to the job: the most shared
        skills first, then the most shared title words.
        """

        title_words = self._title_words(job.title)

        scored_roles = []

        for role in available_jobs:

            role_skills = normalize_skills(role.skills)

            shared_skills = sum(
                1 for skill in matched_skills
                if is_skill_covered(skill, role_skills)
            )
            shared_words = len(title_words & self._title_words(role.role))

            if shared_skills or shared_words:
                scored_roles.append(((shared_skills, shared_words), f"{role.role} ({role.category})"))

        scored_roles.sort(key=lambda item: item[0], reverse=True)

        relevant_roles = []

        # The PDF lists some roles twice (e.g. "IT Technician")
        for _, name in scored_roles:
            if name not in relevant_roles:
                relevant_roles.append(name)

            if len(relevant_roles) == limit:
                break

        return relevant_roles

    def _title_words(self, title: str) -> set[str]:

        words = re.findall(r"[a-z0-9+#]+", (title or "").lower())

        return {word for word in words if word not in TITLE_STOPWORDS}
