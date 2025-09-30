from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import jobs
from .routes import auth

app = FastAPI(title="Job Board API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])


@app.get("/")
def read_root():
    return {"message": "Job Board API is running"}
