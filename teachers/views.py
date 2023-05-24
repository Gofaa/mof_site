from .models import Teachers
from .serializers import TeachersSerializers
from rest_framework import generics


# Create your views here.


class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers


class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers
