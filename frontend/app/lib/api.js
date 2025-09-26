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
