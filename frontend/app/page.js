"use client";
import { useEffect, useState } from "react";
import { fetchJobs, getAuthToken } from "./lib/api";
import JobCard from "../components/JobCard";
import { useRouter } from "next/navigation";
import CreateJobForm from "../components/CreateJobForm";
import LogoutButton from "../components/LogoutButton";

export default function Home() {
  const router = useRouter();
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = getAuthToken();
    if (!token) {
      router.push("/login");
      return;
    }
    // Pass the token to fetchJobs
    fetchJobs(token)
      .then((data) => {
        setJobs(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching jobs:", err);
        setLoading(false);
      });
  }, [router]);

  // Callback when new job is created
  const handleJobCreated = (newJob) => {
    setJobs([newJob, ...jobs]); // Add new job to top of list
  };

  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center p-6">
      {/* Header with Logout Button */}
      <div className="w-full max-w-4xl flex justify-between items-center mb-6">
        <h1 className="text-4xl md:text-5xl font-bold text-blue-600 flex-1 text-center">
          Job Board
        </h1>
        <LogoutButton />
      </div>

      {/* Create Job Form */}
      <div className="w-full max-w-2xl mb-8">
        <CreateJobForm onCreated={handleJobCreated} />
      </div>

      {/* Jobs List */}
      {loading ? (
        <p className="text-lg text-gray-800 mb-6">Loading jobs...</p>
      ) : jobs.length === 0 ? (
        <p className="text-lg text-gray-800 mb-6">No jobs available.</p>
      ) : (
        <div className="w-full max-w-4xl grid gap-6 md:grid-cols-2">
          {jobs.map((job) => (
            <div key={job.id} className="border rounded-lg p-4 bg-white shadow hover:shadow-lg transition">
              <h2 className="text-xl font-semibold text-gray-800">{job.role}</h2>
              <p className="text-gray-600">{job.company}</p>
              <p className="text-sm text-gray-500">{job.location}</p>
              <p className="text-sm text-gray-400 mt-2">
                Posted by: {job.owner_email || "Unknown"}
              </p>
              {job.description && (
                <p className="text-sm text-gray-600 mt-2">{job.description}</p>
              )}
              <a
                href={job.link}
                target="_blank"
                rel="noreferrer"
                className="text-blue-500 hover:underline mt-2 inline-block"
              >
                Apply
              </a>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}