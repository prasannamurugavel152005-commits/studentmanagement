from django.contrib import admin
from django.urls import path, include
from students.views import api_status

urlpatterns = [
    path('', api_status),
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'api/',
        include('students.urls')
    ),
]
