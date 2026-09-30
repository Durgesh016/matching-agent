from app.services.jooble_job_source import JoobleJobSource

source = JoobleJobSource()

jobs = source.get_jobs(role="python developer", location="Hyderabad")

print(f"\nJobs found: {len(jobs)}")

for job in jobs[:5]:

    print("\n-----------------------------")

    print("Title    :", job.title)
    print("Company  :", job.company)
    print("Location :", job.location)
    print("Posted   :", job.posted_date)
    print("URL      :", job.source_url)
    print("Description:", job.description)
