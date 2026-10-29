# Student Management System

A separate HTML/CSS/JavaScript frontend and Django REST backend.

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

## Separate Vercel deployments

- Import the repository and set the frontend project's **Root Directory** to `frontend`.
- Create a second project and set its **Root Directory** to `backend`.
- Configure Django environment variables in the backend project.
- Set `frontend/config.js` to the deployed backend URL, commit, and redeploy.

For persistent production data, use a hosted MySQL database and provide `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`.
