# Day 8 Journal — Job Board Project

**Date:** 2025-10-02  
**Time spent:** 60 minutes

## What I did today

- Added notification subscription model and DB migration.
- Implemented backend routes to subscribe, retrieve own subscription, and send a test notification.
- Added a simple email sending utility (console fallback + SMTP support).
- Built a small frontend component to toggle email notifications and send a test.
- Tested subscription + test-email flow via frontend and PowerShell.

## Notes / Learnings

- Learned how to add new SQLAlchemy models and run Alembic autogenerate.
- Learned to integrate BackgroundTasks for non-blocking work.
- SMTP is configured via `.env` for real emails; dev fallback prints to console.

## Next steps

- Integrate Twilio / WhatsApp provider for SMS/WhatsApp in Day 12+.
- Hook notification send on real job creation (when scraping/APIs are connected).
