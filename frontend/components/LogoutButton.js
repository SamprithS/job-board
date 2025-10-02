// frontend/components/LogoutButton.js
"use client";

import { useRouter } from "next/navigation";

export default function LogoutButton() {
  const router = useRouter();

  function handleLogout() {
    // Clear token from localStorage
    if (typeof window !== "undefined") {
      localStorage.removeItem("access_token");
    }
    // Redirect to login page
    router.push("/login");
  }

  return (
    <button
      onClick={handleLogout}
      className="px-4 py-2 rounded bg-red-500 text-white hover:bg-red-600 transition"
    >
      Logout
    </button>
  );
}