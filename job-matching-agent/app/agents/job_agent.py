import re

from app.services.pdf_service import extract_text_from_pdf
from app.models.schemas import Job

# A category header such as "IT Support:" or
# "PL/SQL developer:(Procedural Language/...)".
# Times such as "3:32 PM" are not headers.
CATEGORY_PATTERN = re.compile(r"^(?!\d{1,2}:\d{2})([^:]+):\s*(?:\(.*\))?$")

NUMBERED_PATTERN = re.compile(r"^\d+\.\s*(.+)$")

# Words that are not skills, e.g. from "(e.g., Facebook, etc)"
JUNK_SKILLS = {"e.g", "eg", "etc", "i.e", "ie"}


class JobAgent:

    def read_jobs_pdf(self, pdf_path: str) -> str:
        return extract_text_from_pdf(pdf_path)

    def extract_jobs(self, pdf_text: str) -> list[Job]:

        # The PDF contains zero-width spaces after the
        # numbers ("1.​ IT Support") and narrow
        # no-break spaces.
        pdf_text = re.sub(r"[​‌‍﻿]", "", pdf_text)
        pdf_text = re.sub(r"[  ]", " ", pdf_text)

        jobs = []
        current_category = None

        # (category, text) of the role being read.
        # The category is stored when the role starts,
        # so the last role of a section keeps its own
        # category.
        current_job = None

        def save_current_job():
            if current_job:
                job = self._create_job(*current_job)

                # Entries without skills (job-board names,
                # notes) are not useful for matching.
                if job.skills:
                    jobs.append(job)

        for line in pdf_text.splitlines():

            line = line.strip()

            if not line:
                continue

            # Ignore PDF page markers
            if line.startswith("--- Page"):
                continue

            # Detect a new numbered job
            match = NUMBERED_PATTERN.match(line)

            if match:
                save_current_job()

                current_job = (
                    (current_category, match.group(1).strip())
                    if current_category
                    else None
                )
                continue

            # Detect category
            category_match = CATEGORY_PATTERN.match(line)

            if category_match:
                save_current_job()
                current_job = None
                current_category = category_match.group(1).strip()
                continue

            # Continuation of previous job. Text outside a
            # role (state lists, notes) is ignored.
            if current_job:
                current_job = (current_job[0], current_job[1] + " " + line)

        # Save last job
        save_current_job()

        return jobs

    def _create_job(self, category: str, job_text: str) -> Job:

        role, skills_text = self._split_role_and_skills(job_text)

        skills = []

        for skill in self._split_skills(skills_text):
            if skill.lower() not in JUNK_SKILLS:
                skills.append(skill)

        return Job(category=category, role=role, skills=skills)

    def _split_role_and_skills(self, job_text: str) -> tuple[str, str]:
        """
        Split "Role - skill1,skill2" into role and skills.

        The PDF is inconsistent: "Role - skills", "Role-skills",
        "Role- skills", "Lead - AI Data Center - skills" and
        "Admin, Linux-skills" all appear. The separator is the
        last hyphen before the first comma (preferring one with
        spaces on both sides), or the first hyphen when the
        role itself contains a comma.
        """

        hyphens = [index for index, char in enumerate(job_text) if char == "-"]

        if not hyphens:
            return job_text.strip(), ""

        first_comma = job_text.find(",")

        if first_comma == -1:
            first_comma = len(job_text)

        before_comma = [index for index in hyphens if index < first_comma]

        spaced = [
            index
            for index in before_comma
            if job_text[index - 1 : index].isspace()
            and job_text[index + 1 : index + 2].isspace()
        ]

        if spaced:
            separator = spaced[-1]
        elif before_comma:
            separator = before_comma[-1]
        else:
            separator = hyphens[0]

        return job_text[:separator].strip(), job_text[separator + 1 :].strip()

    def _split_skills(self, skills_text: str) -> list[str]:

        # "CRM platforms(HubSpot,Salesforce)" and
        # "Microsoft Word & Outlook" list several skills.
        skills_text = re.sub(r"[()]|\s&\s", ",", skills_text)

        # Typos such as "C++.embedded Linux". Short endings
        # like "Node.js" or "ASP.NET" are kept together.
        skills_text = re.sub(r"\.(?=[A-Za-z]{4,})", ",", skills_text)

        skills = []

        for skill in skills_text.split(","):

            skill = skill.strip(" .;:-")

            if skill:
                skills.append(skill)

        return skills
