from django.contrib import admin
from django.urls import path, include
from .views import index
from rest_framework import routers
from news import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MOF SITE",
        default_version='V1',
        description='about mof',
        contact=openapi.Contact(email='asadovgofur@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/news/', include('news.urls')),
    path('api/students/', include('students.urls')),
    path('api/teachers/', include('teachers.urls')),
    path('api/class_table/', include('class_schedule.urls')),
    path('api/listeners/', include('listeners.urls')),


    #swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='swagger-swagger-ui'),
]
