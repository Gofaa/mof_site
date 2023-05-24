from django.urls import path
from .views import ActiveStudentsListView, InActiveStudentsListView, ActiveStudentDetailView, InActiveStudentDetailView


urlpatterns = [
    path('active/', ActiveStudentsListView.as_view()),
    path('inactive/', InActiveStudentsListView.as_view()),
    path('active/detail/<int:pk>/', ActiveStudentDetailView.as_view()),
    path('inactive/detail/<int:pk>/', InActiveStudentDetailView.as_view()),
]