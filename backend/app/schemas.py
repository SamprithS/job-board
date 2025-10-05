# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import enum


# ===== Application Status Enum =====
class ApplicationStatus(str, enum.Enum):
    applied = "applied"
    reviewed = "reviewed"
    accepted = "accepted"
    rejected = "rejected"


# ===== Job Schemas =====
class JobBase(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    description: Optional[str] = None
    url: str
    source: Optional[str] = None
    date_posted: Optional[datetime] = None


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ===== User Schemas =====
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = {"from_attributes": True}


# ===== Auth Schemas =====
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# ===== Application Schemas =====
class ApplicationCreate(BaseModel):
    job_id: int


class ApplicationOut(BaseModel):
    id: int
    job_id: int
    user_id: int
    status: ApplicationStatus
    created_at: datetime

    model_config = {"from_attributes": True}


class ApplicationUpdate(BaseModel):
    status: ApplicationStatus


# ===== Bookmark Schemas =====
class BookmarkCreate(BaseModel):
    job_id: int


class BookmarkOut(BaseModel):
    id: int
    job_id: int
    user_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
