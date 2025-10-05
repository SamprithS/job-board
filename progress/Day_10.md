# Day 10 Journal — Job Board Project

**Date:** 05-10-2025  
**Time spent:** 90 minutes

## What I did today

- Refactored the backend to completely remove all employer-related logic.
- Cleaned up the `models.py` file — now contains only `User`, `Job`, `Application`, and `Bookmark` models.
- Updated `schemas.py` and routes to reflect the new job aggregator architecture.
- Simplified `/jobs` API to be **read-only**, pulling jobs from the database only (no manual posting).
- Created a `seed_jobs.py` script to populate the database with sample **tech jobs** from Google and Microsoft.
- Verified `/jobs` endpoints via PowerShell and tested frontend job listings after schema alignment.

## Notes / Learnings

- Learned how to safely refactor a SQLAlchemy model while keeping schema consistency.
- Understood the difference between an **aggregator platform** (data from external sources) and an **employer-driven portal**.
- Gained confidence in handling full-model rewrites and resetting a dev database using SQLAlchemy.
- Practiced proper Git versioning habits before major refactors.

## Next steps

- **Day 11:** Implement basic web scrapers (starting with Google Careers) to automatically fetch tech job openings.
- **Day 12:** Add an email + WhatsApp notification system for new job alerts to job seekers.
- **Day 13:** Automate scraper runs with a scheduler (e.g., APScheduler or Celery beat).  
   """
  <<<<<<< HEAD

=======

> > > > > > > aaa3a43 (Day 10: Updated Journal)
