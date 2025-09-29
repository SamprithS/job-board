"use client"; // must be the first line

import { useEffect, useState } from "react";
import { fetchJobs, getAuthToken } from "./lib/api"; // make sure this path is correct
import JobCard from "../components/JobCard"; // import your JobCard component
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch jobs from backend
  useEffect(() => {
    const token = getAuthToken();
    if (!token) {
      router.push("/login");
      return;
    }
    fetchJobs()
      .then((data) => {
        setJobs(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching jobs:", err);
        setLoading(false);
      });
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center p-6">
  <h1 className="text-4xl md:text-5xl font-bold text-blue-600 mb-6 text-center">
    Job Board
  </h1>

  {loading ? (
    <p className="text-lg text-gray-800 mb-6">Loading jobs...</p>
  ) : jobs.length === 0 ? (
    <p className="text-lg text-gray-800 mb-6">No jobs available.</p>
  ) : (
    <div className="w-full max-w-4xl grid gap-6 md:grid-cols-2">
      {jobs.map((job) => (
        <JobCard
          key={job.id}
          title={job.role}
          company={job.company}
          location={job.location}
          url={job.link}
        />
      ))}
    </div>
  )}
</main>

  );
}


