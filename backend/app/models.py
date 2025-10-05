# backend/app/models.py
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Text,
    Enum as SAEnum,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


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
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    applications = relationship(
        "Application", back_populates="user", cascade="all, delete-orphan"
    )
    bookmarks = relationship(
        "Bookmark", back_populates="user", cascade="all, delete-orphan"
    )


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    company = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True, nullable=False)  # Official job posting link
    source = Column(
        String, index=True, nullable=True
    )  # e.g., "Google Careers", "LinkedIn"
    date_posted = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    applications = relationship(
        "Application", back_populates="job", cascade="all, delete-orphan"
    )
    bookmarks = relationship(
        "Bookmark", back_populates="job", cascade="all, delete-orphan"
    )


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
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")

    __table_args__ = (UniqueConstraint("job_id", "user_id", name="unique_user_job"),)


class Bookmark(Base):
    __tablename__ = "bookmarks"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="bookmarks")
    job = relationship("Job", back_populates="bookmarks")

    __table_args__ = (
        UniqueConstraint("job_id", "user_id", name="unique_user_bookmark"),
    )


class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, nullable=False)
    revoked_at = Column(DateTime(timezone=True), server_default=func.now())
