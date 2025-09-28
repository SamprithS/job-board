# backend/app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).order_by(models.Job.created_at.desc()).offset(skip).limit(limit).all()

def create_job_if_new(db: Session, job: schemas.JobCreate):
    existing = db.query(models.Job).filter(models.Job.link == job.link).first()
    if existing:
        return existing
    db_job = models.Job(
        company=job.company,
        role=job.role,
        location=job.location,
        link=job.link,
        date_posted=job.date_posted or datetime.utcnow()
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
