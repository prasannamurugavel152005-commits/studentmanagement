from django.contrib import admin
from django.core.management import call_command
from django.http import JsonResponse
from django.urls import include, path


def api_root(request):
    return JsonResponse({
        "status": "online",
        "service": "Student Management System API",
        "endpoints": {
            "students": "/api/students/",
            "admin": "/admin/",
            "migrate": "/api/migrate/"
        }
    })


def run_migrations(request):
    try:
        call_command('migrate', interactive=False)
        return JsonResponse({
            "status": "success",
            "message": "Migrations executed successfully."
        })
    except Exception as exc:
        return JsonResponse({
            "status": "error",
            "message": str(exc)
        }, status=500)


urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/migrate/', run_migrations, name='api-migrate'),
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
]
