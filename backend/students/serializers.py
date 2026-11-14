from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    register_number = serializers.CharField(required=True, allow_blank=False, max_length=30)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
