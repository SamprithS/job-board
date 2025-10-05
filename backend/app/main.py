# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import jobs

app = FastAPI(
    title="Tech Jobs Aggregator API",
    description="API for aggregating tech jobs from top companies in Bangalore",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include only jobs router
app.include_router(jobs.router, prefix="/api", tags=["jobs"])


@app.get("/")
def read_root():
    return {
        "message": "Tech Jobs Aggregator API",
        "status": "active",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
