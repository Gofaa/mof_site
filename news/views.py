from .models import News
from .serializers import NewsSerializer
from rest_framework import generics

# Create your views here.


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'



