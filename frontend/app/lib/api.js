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

export function getAuthToken() {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("access_token");
}

export function clearAuthToken() {
  if (typeof window === "undefined") return;
  localStorage.removeItem("access_token");
}

// Fetch jobs
export async function fetchJobs() {
  try {
    const token = getAuthToken();
    const headers = token ? { "Authorization": `Bearer ${token}` } : {};
    const res = await fetch("http://127.0.0.1:8000/jobs/", { headers });
    if (!res.ok) {
      // If unauthorized, return empty or allow frontend to redirect
      throw new Error(`HTTP ${res.status}`);
    }
    const data = await res.json();
    return data;
  } catch (error) {
    console.error("Error fetching jobs:", error);
    return [];
  }
}



