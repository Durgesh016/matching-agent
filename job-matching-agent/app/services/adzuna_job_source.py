import os
import requests
from dotenv import load_dotenv

from app.models.schemas import JobPosting
from app.services.job_source import JobSource

load_dotenv()

# Countries supported by Adzuna: name -> code used in the URL
ADZUNA_COUNTRIES = {
    "united states": "us",
    "usa": "us",
    "us": "us",
    "america": "us",
    "india": "in",
    "united kingdom": "gb",
    "uk": "gb",
    "england": "gb",
    "canada": "ca",
    "australia": "au",
    "new zealand": "nz",
    "singapore": "sg",
    "south africa": "za",
    "germany": "de",
    "france": "fr",
    "netherlands": "nl",
    "italy": "it",
    "spain": "es",
    "austria": "at",
    "belgium": "be",
    "switzerland": "ch",
    "poland": "pl",
    "brazil": "br",
    "mexico": "mx",
}


def resolve_country(value: str, allow_codes: bool = True) -> str | None:
    """
    Turn "India", "UK" or "in" into an Adzuna country code.

    With allow_codes=False only full names (and USA/US/UK)
    are accepted, so a state such as "CA" (California) is
    not mistaken for Canada.
    """

    value = value.strip().lower()

    if value in ADZUNA_COUNTRIES:
        return ADZUNA_COUNTRIES[value]

    if allow_codes and value in ADZUNA_COUNTRIES.values():
        return value

    return None


class AdzunaJobSource(JobSource):

    def __init__(self, country: str = "us"):
        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_APP_KEY")
        self.country = country

        if not self.app_id:
            raise ValueError("ADZUNA_APP_ID is missing from .env")

        if not self.app_key:
            raise ValueError("ADZUNA_APP_KEY is missing from .env")

    def get_jobs(
        self, role: str = "IT", location: str = "", page: int = 1
    ) -> list[JobPosting]:

        url = f"https://api.adzuna.com/v1/api/jobs/{self.country}/search/{page}"

        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": 20,
            "content-type": "application/json",
        }

        # Empty values would be sent as "what=" / "where="
        if role:
            params["what"] = role

        if location:
            params["where"] = location

        response = requests.get(url, params=params, timeout=30)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get("results", []):

            location_data = item.get("location", {})

            if isinstance(location_data, dict):
                job_location = location_data.get("display_name", location)
            else:
                job_location = location

            company_data = item.get("company", {})

            if isinstance(company_data, dict):
                company = company_data.get("display_name", "Unknown")
            else:
                company = "Unknown"

            job = JobPosting(
                title=item.get("title", ""),
                company=company,
                location=job_location,
                experience=None,
                posted_date=item.get("created"),
                posted_datetime=item.get("created"),
                description=item.get("description", ""),
                skills=[],
                source_url=item.get("redirect_url"),
            )

            jobs.append(job)

        return jobs
