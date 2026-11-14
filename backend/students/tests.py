from django.test import TestCase
from rest_framework.test import APIClient

from .models import Student


class StudentApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_student_can_be_created_through_api(self):
        payload = {
            'register_number': 'REG-1001',
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'age': 20,
            'gender': 'Female',
            'department': 'Computer Science',
            'course': 'BSc Computing',
            'phone': '5551234567',
        }

        response = self.client.post('/api/students/', payload, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'Alice Johnson')

    def test_student_search_matches_multiple_fields(self):
        Student.objects.create(
            register_number='REG-5001',
            name='Bob Lewis',
            email='bob@example.com',
            age=22,
            gender='Male',
            department='Engineering',
            course='Mechanical Engineering',
            phone='5557654321',
        )

        response = self.client.get('/api/students/?search=engineering')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Bob Lewis')
