from django.test import TestCase
from rest_framework.test import APIClient

from .models import Student


class StudentApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_student_can_be_created_through_api(self):
        payload = {
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'age': 20,
            'course': 'BSc Computing',
        }

        response = self.client.post('/api/students/', payload, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'Alice Johnson')

    def test_student_can_be_updated_and_deleted_through_api(self):
        student = Student.objects.create(
            name='Bob Lewis',
            email='bob@example.com',
            age=22,
            course='Mechanical Engineering',
        )

        response = self.client.put(
            f'/api/students/{student.id}/',
            {
                'name': 'Robert Lewis',
                'email': 'bob@example.com',
                'age': 23,
                'course': 'Engineering',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Robert Lewis')

        response = self.client.delete(f'/api/students/{student.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Student.objects.filter(id=student.id).exists())
