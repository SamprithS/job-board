"use client";

import { useState } from "react";
import { createJob } from "../app/lib/api";

export default function CreateJobForm({ onCreated }) {
  const [form, setForm] = useState({ 
    company: "", 
    role: "", 
    location: "", 
    link: "", 
    description: "" 
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    
    const token = localStorage.getItem("access_token");
    if (!token) {
      setError("You must be logged in to create a job");
      setLoading(false);
      return;
    }

    try {
      const job = await createJob(form, token);
      onCreated(job);
      setForm({ company: "", role: "", location: "", link: "", description: "" });
    } catch (err) {
      setError(err.message || "Error creating job");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={submit} className="bg-white p-6 rounded-lg shadow-md space-y-4">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Post a New Job</h2>
      
      <input 
        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={form.company} 
        onChange={(e) => setForm({...form, company: e.target.value})} 
        placeholder="Company *"
        required
      />
      
      <input 
        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={form.role} 
        onChange={(e) => setForm({...form, role: e.target.value})} 
        placeholder="Role *"
        required
      />
      
      <input 
        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={form.location} 
        onChange={(e) => setForm({...form, location: e.target.value})} 
        placeholder="Location"
      />
      
      <input 
        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={form.link} 
        onChange={(e) => setForm({...form, link: e.target.value})} 
        placeholder="Apply link *"
        type="url"
        required
      />
      
      <textarea 
        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        value={form.description} 
        onChange={(e) => setForm({...form, description: e.target.value})} 
        placeholder="Job description"
        rows="4"
      />

      {error && <p className="text-red-600 text-sm">{error}</p>}
      
      <button 
        type="submit" 
        disabled={loading}
        className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition"
      >
        {loading ? "Creating..." : "Create Job"}
      </button>
    </form>
  );
}