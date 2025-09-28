// frontend/lib/api.js
// Handles all backend requests

// Fetch a simple hello message from the backend
export async function fetchHello() {
  try {
    const res = await fetch("http://127.0.0.1:8000/"); // FastAPI backend URL
    if (!res.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await res.json();
    return data.message;
  } catch (error) {
    console.error("Error fetching backend:", error);
    return "Error connecting to backend";
  }
}

// Fetch the list of jobs from the backend
export async function fetchJobs() {
  try {
    const res = await fetch("http://127.0.0.1:8000/jobs/"); // FastAPI backend URL
    if (!res.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await res.json();
    return data; // should be an array of job objects
  } catch (error) {
    console.error("Error fetching jobs:", error);
    return [];
  }
}
