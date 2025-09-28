# backend/app/routes/jobs.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, Base
from .. import models, schemas, crud

router = APIRouter()

# create tables if they don't exist (dev convenience)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip, limit)

@router.post("/", response_model=schemas.Job)
def create_job(job_in: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job_if_new(db, job_in)
