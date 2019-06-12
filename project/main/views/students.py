from project.main.models import Student
from rest_framework import viewsets
from project.main.serializers.students import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
