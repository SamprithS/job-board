# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    company: str
    role: str
    location: str
    link: str

class JobCreate(JobBase):
    date_posted: Optional[datetime] = None

class Job(JobBase):
    id: int
    date_posted: Optional[datetime]
    created_at: datetime

    model_config = {
        "from_attributes": True  # replaces orm_mode in Pydantic v2
    }
