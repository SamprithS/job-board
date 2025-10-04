# Day 9 Journal — Job Board Project

**Date:** 04-10-2025  
**Time spent:** 90 minutes

## What I did today

- Added `Application` model and Alembic migration.
- Built endpoints for job seekers to apply for jobs.
- Built endpoint for job seekers to see their own applications.
- Built endpoint for employers to see applications for their jobs.
- Tested with sample users (employer + job seeker).

## Notes / Learnings

- Learned to define one-to-many relationships in SQLAlchemy with `back_populates`.
- Learned how to prevent duplicate records via query filtering.
- Understood how to enforce role-based restrictions in routes.

## Next steps

- Day 10: Hook up notifications so employers get notified when a new application comes in.
- Day 11: Build employer dashboard to manage applications (review, accept, reject).
