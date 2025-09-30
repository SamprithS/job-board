# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)  # e.g. "SWE I"
    location = Column(String, nullable=True)  # e.g. "Bangalore, India"
    link = Column(String, nullable=True)  # official apply URL
    description = Column(Text, nullable=True)
    date_posted = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
