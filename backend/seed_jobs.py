# backend/seed_jobs.py
from app.database import engine, Base, SessionLocal
from app import models
from datetime import datetime


def seed():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Sample tech jobs with proper dedupe by URL
        sample_jobs = [
            {
                "title": "Software Engineer I - Backend",
                "company": "Google",
                "location": "Bangalore, India",
                "description": "Work on backend systems with Python and Go. Experience with distributed systems preferred.",
                "url": "https://careers.google.com/jobs/sample-job-google-1",
                "source": "Google Careers",
                "date_posted": datetime.utcnow(),
            },
            {
                "title": "Software Engineer I",
                "company": "Microsoft",
                "location": "Bangalore, India",
                "description": "Entry level SWE role working on Azure cloud services.",
                "url": "https://careers.microsoft.com/sample-job-microsoft-1",
                "source": "Microsoft Careers",
                "date_posted": datetime.utcnow(),
            },
            {
                "title": "Backend Developer",
                "company": "Amazon",
                "location": "Hyderabad, India",
                "description": "Build scalable backend services for AWS products.",
                "url": "https://amazon.jobs/sample-job-amazon-1",
                "source": "Amazon Jobs",
                "date_posted": datetime.utcnow(),
            },
            {
                "title": "Full Stack Engineer",
                "company": "Netflix",
                "location": "Remote",
                "description": "Work on streaming infrastructure with React and Node.js.",
                "url": "https://jobs.netflix.com/sample-job-netflix-1",
                "source": "Netflix Jobs",
                "date_posted": datetime.utcnow(),
            },
        ]

        added_count = 0
        for j in sample_jobs:
            # Check if job already exists by URL
            exists = db.query(models.Job).filter(models.Job.url == j["url"]).first()
            if exists:
                print(f"Already exists: {j['url']}")
                continue

            # Create new job
            job = models.Job(
                title=j["title"],
                company=j["company"],
                location=j["location"],
                description=j["description"],
                url=j["url"],
                source=j["source"],
                date_posted=j["date_posted"],
            )
            db.add(job)
            added_count += 1
            print(f"Added: {j['title']} at {j['company']}")

        db.commit()
        print(f"\n✓ Seeded {added_count} new jobs successfully.")

    except Exception as e:
        print(f"Error seeding jobs: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed()
