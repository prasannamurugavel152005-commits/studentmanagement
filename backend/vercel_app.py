import os
import sys
import traceback
from pathlib import Path

# Ensure the backend directory is in sys.path so config and students can be resolved
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as exc:
    error_message = traceback.format_exc()
    print("FATAL ERROR INITIALIZING DJANGO ON VERCEL:\n", error_message, flush=True)

    def app(environ, start_response):
        start_response('500 Internal Server Error', [('Content-Type', 'application/json')])
        return [
            f'{{"error": "Django failed to initialize on Vercel", "details": "{str(exc)}"}}\n'.encode('utf-8')
        ]
