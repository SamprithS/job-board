# backend/app/schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import enum


# ===== User Role Enum =====
class UserRole(str, enum.Enum):
    job_seeker = "job_seeker"
    employer = "employer"


# ===== Application Status Enum =====
class ApplicationStatusEnum(str, enum.Enum):
    applied = "applied"
    reviewed = "reviewed"
    accepted = "accepted"
    rejected = "rejected"


# ===== Job Schemas =====
class JobBase(BaseModel):
    company: str = Field(..., example="Google")
    role: str = Field(..., example="Software Engineer")
    location: str = Field(..., example="Bangalore, India")
    link: str = Field(..., example="https://careers.google.com/job123")
    description: Optional[str] = Field(
        None, example="Work with cutting-edge technology"
    )


class JobCreate(JobBase):
    date_posted: Optional[datetime] = Field(None, example="2025-09-29T00:00:00Z")


class Job(JobBase):
    id: int
    date_posted: Optional[datetime]
    created_at: datetime
    owner_id: Optional[int] = None
    owner_email: Optional[EmailStr] = None

    model_config = {"from_attributes": True}


# ===== User Schemas =====
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: UserRole = UserRole.job_seeker  # Default to job_seeker


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool

    model_config = {"from_attributes": True}


# ===== Auth Schemas =====
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# ===== Application Schemas =====
class ApplicationBase(BaseModel):
    job_id: int


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationOut(BaseModel):
    id: int
    job_id: int
    user_id: int
    status: ApplicationStatusEnum
    created_at: datetime

    model_config = {"from_attributes": True}


class ApplicationUpdate(BaseModel):
    status: ApplicationStatusEnum
