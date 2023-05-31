from django.urls import path
from .views import LearningProcessListView, LearningProcessDetailView


urlpatterns = [
    path('', LearningProcessListView.as_view()),
    path('detail/<int:pk>/', LearningProcessDetailView.as_view()),
]