from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        try:
            students = Student.objects.all()
            search = request.query_params.get('search', '').strip()
            if search:
                students = Student.objects.filter(name__icontains=search) | Student.objects.filter(email__icontains=search) | Student.objects.filter(course__icontains=search)
            return Response(StudentSerializer(students.distinct(), many=True).data)
        except Exception as exc:
            return Response(
                {
                    "error": "Database error or tables not yet migrated.",
                    "details": str(exc),
                    "hint": "Visit /api/migrate/ to initialize database tables or verify your database environment variables."
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(StudentSerializer(student).data)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
