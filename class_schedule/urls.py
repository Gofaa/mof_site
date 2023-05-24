from django.urls import path
from .views import ClassScheduleView


urlpatterns = [
    path('', ClassScheduleView.as_view())
]