# app/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ===== Job Schemas =====


class JobBase(BaseModel):
    title: str
    company: str
    location: str
    description: Optional[str] = None
    apply_url: str
    source: Optional[str] = None
    date_posted: Optional[datetime] = None


class JobCreate(JobBase):
    """Schema for creating a new job (used by scraper)"""

    s3_key: Optional[str] = None


class JobResponse(JobBase):
    """Schema for job responses"""

    id: int
    date_scraped: datetime
    s3_key: Optional[str] = None
    is_notified: bool

    model_config = {"from_attributes": True}


class JobUpdate(BaseModel):
    """Schema for updating job notification status"""

    is_notified: Optional[bool] = None
