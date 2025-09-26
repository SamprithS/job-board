"use client"; // <-- Required for useState & useEffect in App Router

import { useEffect, useState } from "react";
import { fetchHello } from "./lib/api"; // Make sure path matches your folder

export default function Home() {
  const [backendMessage, setBackendMessage] = useState("Loading...");

  useEffect(() => {
    fetchHello().then((msg) => setBackendMessage(msg));
  }, []);

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1 style={{ fontSize: "2rem", color: "blue" }}>Job Board — Frontend</h1>
      <p>Backend says: <strong>{backendMessage}</strong></p>
    </main>
  );
}
