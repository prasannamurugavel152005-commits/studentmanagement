# Student Management System

The HTML/CSS/JavaScript frontend (`frontend/`) and Django REST API (`backend/`)
remain separate in the repository and can be served together by one Vercel
project.

## Run locally

### Backend

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

The API runs at `http://127.0.0.1:8000/api/students/`.

### Frontend

Serve the `frontend` directory with VS Code Live Server or any static server. The API URL is configured in `frontend/config.js`.

## Deploy frontend and backend together on Vercel

- Import this repository as one Vercel project. Set **Root Directory** to `.`
  (the repository root) and **Framework Preset** to **Other**. The root
  `vercel.json` serves `frontend/` as static files and routes `/api/*` to Django.
- Configure the project environment variables: `SECRET_KEY`, `DEBUG=False`,
  and `ALLOWED_HOSTS=.vercel.app`.
- Configure `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT` for a
  persistent MySQL database. Vercel's local SQLite filesystem is temporary and
  must not be used for production student records.
- After setting up the database, initialize its schema through
  `https://<your-vercel-domain>/api/migrate/`.
- Deploy the project. The frontend calls `/api/students/` on the same domain,
  so the combined deployment does not depend on cross-origin API requests.

The existing `frontend/` and `backend/` Vercel configuration files can still be
used if you intentionally deploy the two directories as separate projects. In
that setup, configure the backend's `CORS_ALLOWED_ORIGINS` to include the
frontend's origin and set the frontend API URL to the backend deployment.
