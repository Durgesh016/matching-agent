import re

YEARS = r"(?:years?|yrs?)"

# Phrases that state the minimum years of experience.
# Group 1 is always the minimum.
YEARS_PATTERNS = [
    # "2-4 years", "3 to 5 yrs", "1–3+ years"
    re.compile(rf"\b(\d{{1,2}})\s*(?:-|–|to)\s*\d{{1,2}}\s*\+?\s*{YEARS}\b"),
    # "3+ years"
    re.compile(rf"\b(\d{{1,2}})\s*\+\s*{YEARS}\b"),
    # "minimum 2 years", "at least 3 yrs", "minimum of 4 years"
    re.compile(rf"\b(?:minimum|min\.?|at least)\s+(?:of\s+)?(\d{{1,2}})\s*{YEARS}\b"),
    # "2 years of experience", "4 years' IT support experience".
    # "experience" is required so "30 years in business" is ignored.
    re.compile(rf"\b(\d{{1,2}})\s*{YEARS}['’]?\s+(?:of\s+)?(?:[\w/+-]+\s+){{0,3}}?experience\b"),
]

INTERNSHIP_TITLE = re.compile(r"\bintern(?:ship)?s?\b")

ENTRY_LEVEL = re.compile(
    r"\bentry[- ]level\b|\bfreshers?\b|\bno (?:prior )?experience (?:is )?required\b"
)

ENTRY_LEVEL_TITLE = re.compile(r"\bjunior\b|\bjr\b")


class ExperienceExtractor:

    def extract(
        self,
        text: str,
        title: str = ""
    ) -> str | None:

        title = (title or "").lower()
        text = (text or "").lower()

        # Internship in the title
        if INTERNSHIP_TITLE.search(title):
            return "Internship"

        # Explicit years of experience
        min_years = self._min_years(f"{title} {text}")

        if min_years is not None:
            return self._years_to_level(min_years)

        # Entry level / Fresher / Junior
        if ENTRY_LEVEL.search(f"{title} {text}") or ENTRY_LEVEL_TITLE.search(title):
            return "Entry Level"

        # Only "internship" counts in the description:
        # "mentor our interns" is not an internship.
        if re.search(r"\binternship\b", text):
            return "Internship"

        return None

    def _min_years(self, text: str) -> int | None:
        """
        Minimum years from the first experience phrase
        in the text.
        """

        first_match = None

        for pattern in YEARS_PATTERNS:
            match = pattern.search(text)

            if match and (first_match is None or match.start() < first_match.start()):
                first_match = match

        if first_match is None:
            return None

        years = int(first_match.group(1))

        return years if years <= 30 else None

    def _years_to_level(self, years: int) -> str:

        if years < 1:
            return "0-1 years"

        if years < 3:
            return "1-3 years"

        if years < 5:
            return "3-5 years"

        return "5+ years"
