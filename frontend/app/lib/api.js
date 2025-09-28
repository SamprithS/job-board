// "lib/api.js" handles all backend requests

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

// ✅ New function to fetch jobs
export async function fetchJobs() {
  try {
    const res = await fetch("http://127.0.0.1:8000/jobs"); // Endpoint to fetch jobs
    if (!res.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await res.json();
    return data; // This should be an array of job objects
  } catch (error) {
    console.error("Error fetching jobs:", error);
    return []; // Return empty array if something goes wrong
  }
}
