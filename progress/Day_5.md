\# 📅 Day 5 — Job Board Project

\*\*Date:\*\* 2025-09-30  



\## ✅ Tasks Completed

1\. Implemented authentication protection for job endpoints (`/jobs/`).

2\. Created PowerShell-friendly request flow:

&nbsp;  - Register user  

&nbsp;  - Login user → get access token  

&nbsp;  - Use token for authorized requests (`GET`, `POST`, etc.)  

3\. Successfully tested:

&nbsp;  - Register \& login  

&nbsp;  - Create a job  

&nbsp;  - List jobs  

&nbsp;  - Fetch single job by ID  

&nbsp;  - Authorization system working (unauthenticated requests are blocked).  



\## 🐛 Issues Faced \& Fixes

\- Encountered `401 Unauthorized` errors → solved by always passing Bearer token headers.  

\- Internal bcrypt errors earlier → resolved by fixing dependencies and password truncation.  



\## 🚀 Next Steps

\- Move to Day 6: Connect frontend (Next.js) signup/login forms with backend auth API.  

\- Allow authenticated users to post/view jobs through UI instead of PowerShell.



