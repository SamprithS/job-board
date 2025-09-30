import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    # Add missing column
    conn.execute(text("ALTER TABLE jobs ADD COLUMN IF NOT EXISTS description TEXT;"))
    conn.commit()
    print("Column added successfully!")

    # Check what columns exist now
    result = conn.execute(
        text(
            "SELECT column_name FROM information_schema.columns WHERE table_name = 'jobs';"
        )
    )
    print("\nCurrent columns in jobs table:")
    for row in result:
        print(f"  - {row[0]}")
