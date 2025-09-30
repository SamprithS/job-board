from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# ===== Job Schemas =====
class JobBase(BaseModel):
    company: str = Field(..., example="Google")
    role: str = Field(..., example="Software Engineer")
    location: str = Field(..., example="Bangalore, India")
    link: str = Field(..., example="https://careers.google.com/job123")
    description: Optional[str] = Field(
        None, example="Work with cutting-edge technology"
    )  # Add this


class JobCreate(JobBase):
    date_posted: Optional[datetime] = Field(None, example="2025-09-29T00:00:00Z")


class Job(JobBase):
    id: int
    date_posted: Optional[datetime]
    created_at: datetime
    model_config = {"from_attributes": True}


# ===== User Schemas =====
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


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
