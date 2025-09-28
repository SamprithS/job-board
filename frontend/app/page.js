"use client";

import { useEffect, useState } from "react";
import { fetchHello, fetchJobs } from "./lib/api"; // ✅ import fetchJobs
import JobCard from "../components/JobCard";

export default function Home() {
  const [backendMessage, setBackendMessage] = useState("Loading...");
  const [jobs, setJobs] = useState([]); // ✅ state for jobs
  const [loadingJobs, setLoadingJobs] = useState(true);

  useEffect(() => {
    // Fetch hello message
    fetchHello().then((msg) => setBackendMessage(msg));

    // Fetch jobs from backend
    fetchJobs()
      .then((data) => setJobs(data))
      .finally(() => setLoadingJobs(false));
  }, []);

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-blue-600 mb-6">Job Board — Frontend</h1>
      <p className="text-lg text-gray-800 mb-6">
        Backend says: <strong className="text-green-600">{backendMessage}</strong>
      </p>

      {loadingJobs ? (
        <p>Loading jobs...</p>
      ) : jobs.length === 0 ? (
        <p>No jobs found.</p>
      ) : (
        <div className="w-full max-w-3xl space-y-4">
          {jobs.map((job, index) => (
            <JobCard key={index} {...job} />
          ))}
        </div>
      )}
    </main>
  );
}
