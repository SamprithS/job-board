# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
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
        "from_attributes": True  
    }

# --- User schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = {"from_attributes": True}

# --- Token schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
