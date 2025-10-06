# Day 11 Journal — Job Board Project

**Date:** 06-10-2025  
**Time spent:** 120 minutes

## What I did today

- Set up Supabase PostgreSQL database (free tier)
- Removed all employer-related models, routes, and authentication logic
- Created new `Job` model optimized for scraped data with fields: title, company, location, description, apply_url, date_posted, date_scraped, source, s3_key, is_notified
- Connected FastAPI backend to Supabase using SQLAlchemy
- Configured Alembic to work with Supabase (handled special characters in password using URL encoding)
- Generated and applied database migrations successfully
- Updated API routes to be read-only (GET only): /api/jobs, /api/jobs/{id}, /api/companies, /api/stats
- Tested all endpoints successfully with manual test data
- Removed unused files: auth.py, applications.py

## Challenges

- Struggled with Alembic configuration - password contained @ symbol which broke URL parsing
- Learned to use `quote_plus()` from urllib.parse to properly encode special characters in database passwords
- Had to clean up old migration references by dropping alembic_version table in Supabase
- Debugged ConfigParser interpolation errors by bypassing alembic.ini and creating engine directly in env.py

## Notes / Learnings

- Supabase free tier (500 MB storage, 2 GB bandwidth) is more than sufficient for this project
- URL encoding is critical when passwords contain special characters like @, %, #
- Alembic migrations can reference old versions - always clean up alembic_version table when starting fresh
- SQLAlchemy's `pool_pre_ping=True` helps verify connections before using them
- Read-only APIs are simpler - no authentication, authorization, or complex validation needed

## Technical Details

- Database: Supabase PostgreSQL (remote)
- ORM: SQLAlchemy 2.0.23
- Migrations: Alembic 1.12.1
- API Framework: FastAPI 0.104.1
- Total API endpoints: 5 (root, health, jobs list, job detail, companies, stats)

## Next steps

- Day 12: Build Selenium scraper for target companies (Google, Adobe, Microsoft, etc.)
- Set up AWS S3 bucket for storing raw HTML/JSON responses
- Test scraping one company's careers page locally
