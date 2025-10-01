# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship


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
    role = Column(String, index=True, nullable=False)
    location = Column(String, nullable=True)
    link = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    date_posted = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # --- owner relation ---
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", backref="jobs")

    @property
    def owner_email(self):
        return self.owner.email if self.owner else None
