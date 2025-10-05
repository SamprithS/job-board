# app/routes/jobs.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func, or_
from datetime import datetime
from pydantic import BaseModel
from app.database import get_db
from app import models

router = APIRouter()


# Pydantic Response Schema
class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: Optional[str]
    apply_url: str
    date_posted: Optional[datetime]
    date_scraped: datetime
    source: Optional[str]

    class Config:
        from_attributes = True


@router.get("/jobs", response_model=List[JobResponse])
def list_jobs(
    q: Optional[str] = Query(
        None, description="Search in title, description, or company"
    ),
    company: Optional[str] = Query(None, description="Filter by company name"),
    location: str = Query(default="Bangalore", description="Filter by location"),
    source: Optional[str] = Query(
        None, description="Filter by source (e.g., Google Careers, LinkedIn)"
    ),
    limit: int = Query(
        default=50, ge=1, le=200, description="Number of results to return"
    ),
    offset: int = Query(default=0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db),
):
    """
    List all tech jobs with optional filters.
    Default location is Bangalore.
    Jobs are sorted by date_posted (newest first).
    """
    query = db.query(models.Job)

    # Location filter (default: Bangalore)
    query = query.filter(models.Job.location.ilike(f"%{location}%"))

    # Company filter
    if company:
        query = query.filter(models.Job.company.ilike(f"%{company}%"))

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


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get a single job by ID"""
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.get("/companies", response_model=List[str])
def get_companies(db: Session = Depends(get_db)):
    """
    Get list of all companies with active jobs
    """
    companies = (
        db.query(models.Job.company).distinct().order_by(models.Job.company).all()
    )
    return [c[0] for c in companies if c[0]]


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    """
    Get aggregator statistics
    """
    total_jobs = db.query(models.Job).count()
    total_companies = db.query(models.Job.company).distinct().count()

    latest_scrape = (
        db.query(models.Job.date_scraped)
        .order_by(models.Job.date_scraped.desc())
        .first()
    )

    return {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "last_scraped": latest_scrape[0] if latest_scrape else None,
        "status": "active",
    }
