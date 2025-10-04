# backend/app/models.py
import enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
    ForeignKey,
    Enum as SAEnum,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class UserRole(enum.Enum):
    job_seeker = "job_seeker"
    employer = "employer"


class ApplicationStatus(enum.Enum):
    applied = "applied"
    reviewed = "reviewed"
    accepted = "accepted"
    rejected = "rejected"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    # Role column with default job_seeker
    role = Column(
        SAEnum(UserRole, name="user_role", native_enum=False),
        nullable=False,
        default=UserRole.job_seeker,
        server_default="job_seeker",
    )
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    applications = relationship(
        "Application", back_populates="user", cascade="all, delete-orphan"
    )


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
    owner = relationship("User", foreign_keys=[owner_id], backref="jobs")

    # Applications relation
    applications = relationship(
        "Application", back_populates="job", cascade="all, delete-orphan"
    )

    @property
    def owner_email(self):
        return self.owner.email if self.owner else None


class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    status = Column(
        SAEnum(ApplicationStatus, name="application_status", native_enum=False),
        nullable=False,
        default=ApplicationStatus.applied,
        server_default="applied",
    )
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    job = relationship("Job", back_populates="applications")
    user = relationship("User", back_populates="applications")


class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True, nullable=False)
    revoked_at = Column(DateTime, default=datetime.utcnow)
