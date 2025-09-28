# backend/seed_jobs.py
from app.database import SessionLocal, engine, Base
from app import models, schemas, crud
from sqlalchemy.exc import OperationalError

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    sample = [
        {
            "company": "Google",
            "role": "SWE I - Backend",
            "location": "Bangalore, India",
            "link": "https://careers.google.com/jobs/sample-job-google-1",
        },
        {
            "company": "Microsoft",
            "role": "Software Engineer I",
            "location": "Bangalore, India",
            "link": "https://careers.microsoft.com/sample-job-microsoft-1",
        },
    ]
    try:
        for j in sample:
            job_in = schemas.JobCreate(**j)
            crud.create_job_if_new(db, job_in)
        print("Seeded sample jobs.")
    except OperationalError as e:
        print("OperationalError:", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed()
