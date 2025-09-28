# backend/app/routes/jobs.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models import Job as JobModel  # SQLAlchemy model
from app.schemas import Job  # Pydantic schema

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Job])
def read_jobs(db: Session = Depends(get_db)):
    jobs = db.query(JobModel).all()
    return jobs
