from .models import Listeners
from .serializers import ListenersSerializer
from rest_framework import generics

# Create your views here.


class ListenersListView(generics.ListAPIView):
    queryset = Listeners.objects.all()
    serializer_class = ListenersSerializer


class ListenersDetailView(generics.RetrieveAPIView):
    queryset = Listeners.objects.all()
    serializer_class = ListenersSerializer

