# backend/app/routes/jobs.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas
from app.deps import get_current_user, require_employer

router = APIRouter()


# GET /jobs/ -> List jobs (any authenticated user can view)
@router.get("/", response_model=List[schemas.Job], tags=["jobs"])
def read_jobs(
    db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
):
    jobs = db.query(models.Job).order_by(models.Job.created_at.desc()).all()
    return jobs


# GET /jobs/{id} -> Get single job (any authenticated user can view)
@router.get("/{job_id}", response_model=schemas.Job, tags=["jobs"])
def read_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )
    return job


# POST /jobs/ -> Create a job (EMPLOYERS ONLY)
@router.post(
    "/", response_model=schemas.Job, status_code=status.HTTP_201_CREATED, tags=["jobs"]
)
def create_job(
    job_in: schemas.JobCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(
        require_employer
    ),  # Changed to require_employer
):
    job = models.Job(
        company=job_in.company,
        role=job_in.role,
        location=job_in.location,
        link=job_in.link,
        description=job_in.description,
        date_posted=job_in.date_posted,
        owner_id=current_user.id,
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


# DELETE /jobs/{id} -> Delete job (EMPLOYERS ONLY, must be owner)
@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["jobs"])
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(
        require_employer
    ),  # Changed to require_employer
):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
        )

    # Check ownership
    if job.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the owner of this job",
        )

    db.delete(job)
    db.commit()
    return None
