"use client";

import { useEffect, useState } from "react";
import { fetchHello } from "./lib/api";

// ✅ Import JobCard at the top with other imports
import JobCard from "../components/JobCard";

export default function Home() {
  const [backendMessage, setBackendMessage] = useState("Loading...");

  useEffect(() => {
    fetchHello().then((msg) => setBackendMessage(msg));
  }, []);

  // Sample job data (we'll fetch real jobs later)
  const jobs = [
    { title: "SWE I", company: "Example Corp", location: "Bangalore", url: "#" },
    { title: "SDE I", company: "TechCo", location: "Bangalore", url: "#" },
  ];

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-blue-600 mb-6">Job Board — Frontend</h1>
      <p className="text-lg text-gray-800 mb-6">
        Backend says: <strong className="text-green-600">{backendMessage}</strong>
      </p>

      {/* Render JobCards dynamically */}
      <div className="w-full max-w-3xl space-y-4">
        {jobs.map((job, index) => (
          <JobCard key={index} {...job} />
        ))}
      </div>
    </main>
  );
}
