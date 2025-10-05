# backend/app/routes/jobs.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func, or_
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/", response_model=List[schemas.Job])
def list_jobs(
    q: Optional[str] = Query(
        None, description="Search in title, description, or company"
    ),
    location: Optional[str] = Query(None, description="Filter by location"),
    source: Optional[str] = Query(
        None, description="Filter by source (e.g., Google, LinkedIn)"
    ),
    limit: int = Query(50, ge=1, le=200, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db),
):
    """
    List all jobs with optional filters.
    Jobs are sorted by date_posted (newest first).
    """
    query = db.query(models.Job)

    # Search filter - searches in title, description, and company
    if q:
        q_like = f"%{q.lower()}%"
        query = query.filter(
            or_(
                func.lower(models.Job.title).like(q_like),
                func.lower(models.Job.description).like(q_like),
                func.lower(models.Job.company).like(q_like),
            )
        )

    # Location filter
    if location:
        query = query.filter(models.Job.location.ilike(f"%{location}%"))

    # Source filter
    if source:
        query = query.filter(models.Job.source.ilike(f"%{source}%"))

    # Order by date_posted (newest first), handle nulls
    results = (
        query.order_by(models.Job.date_posted.desc().nullslast())
        .offset(offset)
        .limit(limit)
        .all()
    )

    return results


@router.get("/{job_id}", response_model=schemas.Job)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get a single job by ID"""
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
