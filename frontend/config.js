// Configure API Base URL:
// Automatically uses local backend when running on localhost / 127.0.0.1.
// When deployed on Vercel, it connects to your production backend URL.
const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

window.API_BASE_URL = isLocal
  ? "http://127.0.0.1:8000/api/students/"
  : "https://studentmanagement-backend.vercel.app/api/students/";
