# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import jobs, auth, applications

app = FastAPI(title="Job Board API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router)  # Remove prefix="/jobs" - it's already in the router
app.include_router(applications.router)  # Already has prefix in router too


@app.get("/")
def read_root():
    return {"message": "Job Board API is running"}
