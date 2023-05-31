from .serializers import LearningProcessSerializer
from .models import LearningProcess
from rest_framework import generics


# Create your views here.


class LearningProcessListView(generics.ListAPIView):
    queryset = LearningProcess.objects.all()
    serializer_class = LearningProcessSerializer


class LearningProcessDetailView(generics.RetrieveAPIView):
    queryset = LearningProcess.objects.all()
    serializer_class = LearningProcessSerializer

