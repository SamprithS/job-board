# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Validate DATABASE_URL exists
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL not found in .env file!")

# Add SSL mode for Supabase
if "supabase.co" in DATABASE_URL and "sslmode" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL + "?sslmode=require"

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verify connections before using
    echo=False,  # Set to True for debugging SQL queries
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
