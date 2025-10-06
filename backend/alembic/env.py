# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context
import os
import sys
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import your models
from app.database import Base
from app.models import Job

# Alembic Config object
config = context.config

# Build DATABASE_URL from components
password = quote_plus(os.getenv("SUPABASE_PASSWORD", ""))
user = os.getenv("SUPABASE_USER", "postgres")
host = os.getenv("SUPABASE_HOST")
port = os.getenv("SUPABASE_PORT", "5432")
db = os.getenv("SUPABASE_DB", "postgres")

database_url = f"postgresql://{user}:{password}@{host}:{port}/{db}?sslmode=require"

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Create engine directly without using config
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
