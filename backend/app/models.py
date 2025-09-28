# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    link = Column(String, unique=True, nullable=False)
    date_posted = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
