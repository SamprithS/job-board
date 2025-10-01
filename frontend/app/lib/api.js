// frontend/lib/api.js
// Handles all backend requests

// --- Utility functions ---
export function getAuthToken() {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("access_token");
}

export function clearAuthToken() {
  if (typeof window === "undefined") return;
  localStorage.removeItem("access_token");
}

// --- Auth endpoints ---
export async function registerUser(email, password) {
  const res = await fetch("http://127.0.0.1:8000/auth/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
}

export async function loginUser(email, password) {
  const res = await fetch("http://127.0.0.1:8000/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json(); // { access_token, token_type }
}

// --- Jobs endpoints ---
export async function fetchJobs(token = null) {
  const headers = token ? { Authorization: `Bearer ${token}` } : {};
  const res = await fetch("http://127.0.0.1:8000/jobs/", { headers });
  if (!res.ok) throw new Error("Failed to fetch jobs");
  return res.json();
}

export async function fetchJobById(id, token = null) {
  const headers = token ? { Authorization: `Bearer ${token}` } : {};
  const res = await fetch(`http://127.0.0.1:8000/jobs/${id}`, { headers });
  if (!res.ok) throw new Error("Failed to fetch job");
  return res.json();
}

export async function createJob(jobData, token) {
  const res = await fetch("http://127.0.0.1:8000/jobs/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(jobData),
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Failed to create job");
  }
  return res.json();
}

export async function deleteJob(id, token) {
  const res = await fetch(`http://127.0.0.1:8000/jobs/${id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "Failed to delete job");
  }
  return { success: true };
}
