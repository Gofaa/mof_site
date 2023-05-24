from .models import ActiveStudents, InactiveStudents
from .serializers import ActiveStudentsSerializers, InActiveStudentsSerializers
from rest_framework import generics

# Create your views here.


class ActiveStudentsListView(generics.ListAPIView):
    queryset = ActiveStudents.objects.all()
    serializer_class = ActiveStudentsSerializers


class ActiveStudentDetailView(generics.RetrieveAPIView):
    queryset = ActiveStudents.objects.all()
    serializer_class = ActiveStudentsSerializers



class InActiveStudentsListView(generics.ListAPIView):
    queryset = InactiveStudents.objects.all()
    serializer_class = InActiveStudentsSerializers


class InActiveStudentDetailView(generics.RetrieveAPIView):
    queryset = InactiveStudents.objects.all()
    serializer_class = InActiveStudentsSerializers

