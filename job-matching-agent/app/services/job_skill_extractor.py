import re

from app.services.skill_matcher import normalize_skill

# Everyday words from the PDF that appear in almost every
# posting ("email your resume", "follow us on LinkedIn").
# They stay in the profile but are not searched for.
IGNORED_TERMS = {
    "basic",
    "cables",
    "campaigns",
    "collecting data",
    "computer skills",
    "customer engagement",
    "customer satisfaction",
    "data support",
    "documentation",
    "editing",
    "email",
    "emails",
    "formulas",
    "linkedin",
    "maintain documentation",
    "math skills",
    "operations",
    "problem solving",
    "product training",
    "racking",
    "reporting skills",
    "retentions",
    "stacking",
    "teams",
    "tickets",
    "triggers",
    "update databases",
    "views",
    "zoom",
}

# Product names that are also everyday words ("a word",
# "positive outlook", "excel in", "access to") only count
# when capitalized.
CAPITALIZED_ONLY = {"word", "excel", "outlook", "access"}


class JobSkillExtractor:

    def extract_skills_from_pdf_roles(self, available_jobs) -> list[str]:
        """
        Build a unique skill vocabulary from the Roles & Skills PDF.
        """

        skills = set()

        for job in available_jobs:
            for skill in job.skills:
                skill = skill.strip()

                if skill:
                    skills.add(skill)

        return sorted(skills, key=len, reverse=True)

    def load_skill_file(self, file_path: str) -> list[str]:
        """
        Read one skill per line, skipping blank lines
        and # comments.
        """

        skills = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line and not line.startswith("#"):
                    skills.append(line)

        return skills

    def build_vocabulary(self, *skill_lists: list[str]) -> list[str]:
        """
        Merge skill lists, ignoring capitalization (the first
        spelling wins). Longest first, so "SQL Server" is found
        before "SQL".
        """

        vocabulary = {}

        for skills in skill_lists:
            for skill in skills:
                skill = skill.strip()
                key = skill.lower()

                # Single letters ("C") match too much text.
                if len(key) < 2 or key in IGNORED_TERMS:
                    continue

                if key not in vocabulary:
                    vocabulary[key] = skill

        return sorted(vocabulary.values(), key=len, reverse=True)

    def extract(self, text: str, skill_vocabulary: list[str]) -> list[str]:
        """
        Extract skills that explicitly appear
        in the job description.
        """

        if not text:
            return []

        remaining = text

        # normalized skill -> spelling from the vocabulary
        found_skills = {}

        for skill in skill_vocabulary:

            pattern = self._pattern(skill)

            # Blank out the match so "SQL" is not found again
            # inside "SQL Server".
            remaining, count = pattern.subn(
                lambda match: " " * len(match.group()), remaining
            )

            if count:
                found_skills.setdefault(normalize_skill(skill), skill)

        return sorted(found_skills.values(), key=str.lower)

    def _pattern(self, skill: str) -> re.Pattern:

        skill = skill.strip()

        if skill.lower() in CAPITALIZED_ONLY:
            skill = skill.capitalize()
            flags = 0

        # Short acronyms ("UPS", "CAN", "SAP") must be
        # uppercase so "follow-ups" or "you can" don't match.
        elif skill.isupper() and len(skill) <= 4:
            flags = 0

        else:
            flags = re.IGNORECASE

        return re.compile(r"(?<!\w)" + re.escape(skill) + r"(?!\w)", flags)
