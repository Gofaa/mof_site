from django.urls import path
from .views import ListenersListView, ListenersDetailView


urlpatterns = [
    path('', ListenersListView.as_view()),
    path('detail/<int:pk>/', ListenersDetailView.as_view())
    ]