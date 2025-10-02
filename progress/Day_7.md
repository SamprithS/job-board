# Day 7 — Alembic migrations + Logout

**Date:** 2025-10-02

## Completed

- Installed and configured Alembic for DB migrations.
- Connected Alembic to app metadata and .env DATABASE_URL.
- Implemented frontend client-side logout (removes access_token and redirects).
- (Optional) Added server-side token revocation flow and DB model `revoked_tokens` + logout endpoint.

## Next

- Use Alembic for all future DB schema changes.
- Add tests for server-side logout if using token revocation.
- Improve frontend UX for login/logout states and protected pages.
