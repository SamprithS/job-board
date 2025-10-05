# app/models.py

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    company = Column(String(255), index=True, nullable=False)
    location = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    apply_url = Column(String(500), unique=True, nullable=False)

    # Timestamps
    date_posted = Column(DateTime(timezone=True), nullable=True)
    date_scraped = Column(DateTime(timezone=True), server_default=func.now())

    # Metadata
    source = Column(String(255), nullable=True)  # e.g., "Google Careers", "LinkedIn"
    s3_key = Column(String(500), nullable=True)  # Reference to raw data in S3
    is_notified = Column(Boolean, default=False)  # Track if user was notified

    def __repr__(self):
        return f"<Job(id={self.id}, title='{self.title}', company='{self.company}')>"
