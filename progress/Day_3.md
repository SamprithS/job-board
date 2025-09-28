\# Day 3 Journal — Job Board Project



\*\*Date:\*\* 28-Sep-2025  

\*\*Time spent:\*\* 120 minutes  



\## What I did today



\- Implemented backend API to serve job listings using FastAPI

\- Created `Job` SQLAlchemy model and `Job` Pydantic schema

\- Added `/jobs` route with proper database session handling

\- Seeded sample jobs into the database

\- Updated frontend `page.js` to fetch real jobs from the backend

\- Updated `lib/api.js` to handle fetching jobs and a simple hello message

\- Modified `JobCard` component to display job role, company, location, and apply link

\- Applied modern Tailwind styling to job cards (shadows, hover, spacing)

\- Fixed mapping of backend fields (`role` → `title`, `link` → `url`)



\## Notes / Learnings



\- Learned how to connect FastAPI backend with Next.js frontend

\- Pydantic `orm\_mode` / `from\_attributes` is important for returning SQLAlchemy models

\- Learned how to handle async fetch requests in React with `useEffect`

\- Learned to debug CORS and database session issues



\## Next Steps



\- Day 4: Implement login/auth system

\- Add notifications system for new job postings

\- Improve UI/UX for job listings (filters, search, sorting)



