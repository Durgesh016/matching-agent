import re
from datetime import datetime, timezone, timedelta

from app.models.schemas import JobPosting


class JobSearchAgent:

    def search(
        self,
        jobs: list[JobPosting],
        role: str | None = None,
        location: str | None = None,
        experience: str | None = None,
        posted_within: str | None = None,
    ) -> list[JobPosting]:

        results = jobs

        # =========================================
        # ROLE FILTER
        # =========================================

        if role:

            # Every word of the role must appear in the title
            # as a complete word, in any order:
            #
            # "python developer" accepts "Developer - Python"
            # "it" accepts "IT Support", rejects "Physical Therapist"

            role_words = [
                word.strip(".")
                for word in re.findall(r"[\w+#.]+", role.lower())
                if word.strip(".")
            ]

            filtered_results = []

            for job in results:

                title = (job.title or "").strip().lower()

                if all(
                    re.search(rf"(?<!\w){re.escape(word)}(?!\w)", title)
                    for word in role_words
                ):
                    filtered_results.append(job)

            results = filtered_results

        # =========================================
        # LOCATION FILTER
        # =========================================

        # The country is already chosen by the Adzuna
        # URL, so this is a city/state only.

        if location:

            location = location.strip().lower()

            results = [
                job for job in results if location in (job.location or "").lower()
            ]

        # =========================================
        # EXPERIENCE FILTER
        # =========================================

        if experience:

            requested_experience = self.normalize_experience(experience)

            if requested_experience:

                results = [
                    job
                    for job in results
                    if self._experience_matches(job.experience, requested_experience)
                ]

        # =========================================
        # POSTED WITHIN FILTER
        # =========================================

        if posted_within:

            hours = self._get_hours(posted_within)

            if hours is not None:

                cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)

                filtered_results = []

                for job in results:

                    if not job.posted_datetime:
                        continue

                    posted_time = self._parse_datetime(job.posted_datetime)

                    if not posted_time:
                        continue

                    if posted_time >= cutoff:
                        filtered_results.append(job)

                results = filtered_results

        return results

    # =========================================
    # EXPERIENCE NORMALIZATION
    # =========================================

    def normalize_experience(self, experience: str) -> str | None:

        value = experience.lower().strip()

        mappings = {
            "intern": "Internship",
            "internship": "Internship",
            "entry": "Entry Level",
            "entry level": "Entry Level",
            "fresher": "Entry Level",
            "freshers": "Entry Level",
            "0-1": "0-1 years",
            "0-1 years": "0-1 years",
            "0 to 1": "0-1 years",
            "0 to 1 years": "0-1 years",
            "1-3": "1-3 years",
            "1-3 years": "1-3 years",
            "1 to 3": "1-3 years",
            "1 to 3 years": "1-3 years",
            "3-5": "3-5 years",
            "3-5 years": "3-5 years",
            "3 to 5": "3-5 years",
            "3 to 5 years": "3-5 years",
            "5+": "5+ years",
            "5+ years": "5+ years",
        }

        return mappings.get(value)

    # =========================================
    # EXPERIENCE MATCHING
    # =========================================

    def _experience_matches(
        self, job_experience: str | None, requested_experience: str
    ) -> bool:

        # Most postings don't state experience; keep them
        # instead of hiding them.
        if not job_experience:
            return True

        # Entry-level jobs often ask for 0-1 years.
        entry_levels = {"entry level", "0-1 years"}

        job_experience = job_experience.lower()
        requested_experience = requested_experience.lower()

        if job_experience in entry_levels and requested_experience in entry_levels:
            return True

        return job_experience == requested_experience

    # =========================================
    # POSTED WITHIN
    # =========================================

    def _get_hours(self, posted_within: str):

        value = posted_within.lower().strip()

        mapping = {
            "24 hours": 24,
            "1 day": 24,
            "3 days": 72,
            "7 days": 168,
            "14 days": 336,
        }

        return mapping.get(value)

    # =========================================
    # DATETIME PARSING
    # =========================================

    def _parse_datetime(self, value: str):

        try:

            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))

            if parsed.tzinfo is None:

                parsed = parsed.replace(tzinfo=timezone.utc)

            return parsed

        except ValueError:

            return None
