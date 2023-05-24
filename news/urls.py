from django.urls import path
from .views import NewsListApiView, NewsDetailApiView


urlpatterns = [
    path('', NewsListApiView.as_view()),
    path('<slug:slug>/', NewsDetailApiView.as_view(), name='news-detail')
]