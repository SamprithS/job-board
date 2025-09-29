"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

function setAuthToken(token) {
  if (typeof window !== "undefined") localStorage.setItem("access_token", token);
}

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");
  const router = useRouter();

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const res = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      if (!res.ok) {
        const err = await res.json();
        setMsg(err.detail || "Login failed");
        return;
      }
      const data = await res.json();
      setAuthToken(data.access_token);
      setMsg("Login successful! Redirecting...");
      setTimeout(() => router.push("/"), 600);
    } catch (error) {
      console.error(error);
      setMsg("Network error");
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center p-6 bg-gray-50">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md w-full max-w-sm">
        <h2 className="text-2xl mb-4">Login</h2>
        <input className="w-full mb-2 p-2 border rounded" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
        <input type="password" className="w-full mb-2 p-2 border rounded" placeholder="Password" value={password} onChange={e=>setPassword(e.target.value)} />
        <button className="w-full bg-blue-600 text-white p-2 rounded">Login</button>
        <p className="mt-3 text-sm text-red-600">{msg}</p>
      </form>
    </main>
  );
}
