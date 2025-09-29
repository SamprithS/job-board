# backend/app/routes/jobs.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models import Job as JobModel, User  # import User for typing
from app.schemas import Job  # Pydantic schema
from app.deps import get_current_user

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Job])
def read_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 🔐 require login
):
    jobs = db.query(JobModel).all()
    return jobs
