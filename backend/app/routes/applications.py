# backend/app/routes/applications.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.deps import get_db, get_current_user, require_job_seeker
from app.database import get_db

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post(
    "/", response_model=schemas.ApplicationOut, status_code=status.HTTP_201_CREATED
)
def apply_to_job(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(require_job_seeker),  # Only job seekers can apply
):
    """Apply to a job - job seekers only"""
    # Check if job exists
    job = db.query(models.Job).filter(models.Job.id == application.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Prevent duplicate applications
    existing = (
        db.query(models.Application)
        .filter(
            models.Application.job_id == application.job_id,
            models.Application.user_id == user.id,
        )
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="You already applied to this job")

    # Create application
    new_app = models.Application(
        job_id=application.job_id,
        user_id=user.id,
        status=models.ApplicationStatus.applied,
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


@router.get("/my", response_model=List[schemas.ApplicationOut])
def get_my_applications(
    db: Session = Depends(get_db), user: models.User = Depends(get_current_user)
):
    """Get all applications by the current user (job seeker view)"""
    return (
        db.query(models.Application)
        .filter(models.Application.user_id == user.id)
        .order_by(models.Application.created_at.desc())
        .all()
    )


@router.get("/job/{job_id}", response_model=List[schemas.ApplicationOut])
def get_applications_for_job(
    job_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """Get all applications for a specific job - employer only (must be job owner)"""
    # Check if job exists
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    # Only the job owner can view applications
    if job.owner_id != user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to view applications for this job"
        )

    return (
        db.query(models.Application)
        .filter(models.Application.job_id == job_id)
        .order_by(models.Application.created_at.desc())
        .all()
    )


@router.patch("/{application_id}/status", response_model=schemas.ApplicationOut)
def update_application_status(
    application_id: int,
    status_update: schemas.ApplicationUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """Update application status - employer only (must own the job)"""
    # Get application
    application = (
        db.query(models.Application)
        .filter(models.Application.id == application_id)
        .first()
    )
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    # Check if user owns the job
    if application.job.owner_id != user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to update this application"
        )

    # Update status
    application.status = status_update.status
    db.commit()
    db.refresh(application)
    return application
