# Day 6 — Link jobs to users & frontend token wiring

**Date:** 2025-10-01

## Completed

- Added `owner_id` to Job model and relationship to User.
- Assigned owner when creating jobs.
- Prevented non-owner delete (403).
- Frontend sends JWT in Authorization header for protected endpoints.
- Tested register/login/create/list/get/delete flow.

## Next

- Implement job scraping / API integrations (Day 19 planning).
- Improve frontend styling and dashboard pages.
