// frontend/config.js

// 1. Detect if the user is running the app on their local computer
const isLocal = window.location.hostname === "localhost" || 
                window.location.hostname === "127.0.0.1";

// 2. Select the matching backend URL automatically
window.API_BASE_URL = isLocal
  ? "http://127.0.0.1:8000/api/students/"          // LOCAL (Dev)
  : "https://studentmanagement-backend.vercel.app/api/students/"; // PRODUCTION (Vercel)
