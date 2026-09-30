import os
import requests

from dotenv import load_dotenv

from app.models.schemas import JobPosting
from app.services.job_source import JobSource

load_dotenv()


class JoobleJobSource(JobSource):

    def __init__(self):

        self.api_key = os.getenv("JOOBLE_API_KEY")

        if not self.api_key:
            raise ValueError("JOOBLE_API_KEY is missing from .env")

    def get_jobs(
        self, role: str = "python developer", location: str = "Hyderabad", page: int = 1
    ) -> list[JobPosting]:

        url = f"https://in.jooble.org/api/{self.api_key}"

        payload = {
            "keywords": role,
            "location": location,
            "page": page,
            "ResultOnPage": 20,
            "SearchMode": 0,
            "companysearch": False,
        }

        response = requests.post(url, json=payload, timeout=30)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get("jobs", []):

            job = JobPosting(
                title=item.get("title", ""),
                company=item.get("company", "Unknown"),
                location=item.get("location", location),
                experience=None,
                posted_date=self._extract_date(item.get("updated")),
                posted_datetime=item.get("updated"),
                description=item.get("snippet", ""),
                skills=[],
                source_url=item.get("link"),
            )

            jobs.append(job)

        return jobs

    def _extract_date(self, updated):

        if not updated:
            return None

        return updated[:10]
