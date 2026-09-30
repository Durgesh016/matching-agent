from app.services.adzuna_job_source import AdzunaJobSource

source = AdzunaJobSource()

jobs = source.get_jobs(role="IT", location="United States")

print("\nJobs loaded:", len(jobs))

for job in jobs:
    print("\n----------------------------")
    print("Title:", job.title)
    print("Company:", job.company)
    print("Location:", job.location)
    print("Created:", job.posted_datetime)
    print("Description:", job.description[:300])
    print("URL:", job.source_url)
