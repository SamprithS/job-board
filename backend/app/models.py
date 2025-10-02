# backend/app/models.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)
    location = Column(String, nullable=True)
    link = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    date_posted = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Owner relation
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    owner = relationship("User", backref="jobs")

    @property
    def owner_email(self):
        return self.owner.email if self.owner else None


class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True, nullable=False)
    revoked_at = Column(DateTime, default=datetime.utcnow)
