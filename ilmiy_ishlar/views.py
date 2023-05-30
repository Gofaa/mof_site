from .models import ScientificWork
from .serializers import ScientificWorkSerializer
from rest_framework import generics


class ScientificWorksListApiView(generics.ListAPIView):
    queryset = ScientificWork.objects.all()
    serializer_class = ScientificWorkSerializer


class ScientificWorksDetailApiView(generics.RetrieveAPIView):
    queryset = ScientificWork
    serializer_class = ScientificWorkSerializer
