from django.urls import path
from .views import TeachersListView, TeacherDetailView, my_view

urlpatterns = [
    path('', TeachersListView.as_view()),
    path('detail/<int:pk>/', TeacherDetailView.as_view()),
    path('user_agent', my_view, name='my_template'),
]
