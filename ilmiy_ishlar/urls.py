from django.urls import path
from .views import ScientificWorksListApiView, ScientificWorksDetailApiView

urlpatterns = [
    path('', ScientificWorksListApiView.as_view()),
    path('detail/<int:pk>/', ScientificWorksDetailApiView.as_view()),
]