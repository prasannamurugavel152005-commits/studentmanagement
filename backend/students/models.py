from django.db import models


class Student(models.Model):
    register_number = models.CharField(max_length=30, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, default='')
    department = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} ({self.register_number})"
