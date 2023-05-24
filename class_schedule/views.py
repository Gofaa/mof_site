from rest_framework import generics
from .models import ClassSchedule
from .serializers import ClassScheduleSerializer


class ClassScheduleView(generics.ListAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer


