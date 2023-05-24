from django.urls import path
from .views import TeachersListView, TeacherDetailView

urlpatterns = [
    path('', TeachersListView.as_view()),
    path('detail/<int:pk>/', TeacherDetailView.as_view())
]
