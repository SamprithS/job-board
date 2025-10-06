# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

# Build DATABASE_URL from components (handles special characters properly)
if os.getenv("SUPABASE_HOST"):
    # URL-encode the password to handle special characters like @ and %
    password = quote_plus(os.getenv("SUPABASE_PASSWORD", ""))
    user = os.getenv("SUPABASE_USER", "postgres")
    host = os.getenv("SUPABASE_HOST")
    port = os.getenv("SUPABASE_PORT", "5432")
    db = os.getenv("SUPABASE_DB", "postgres")

    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}?sslmode=require"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Database credentials not found in .env file!")

# Create engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
