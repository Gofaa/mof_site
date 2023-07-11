from .models import Teachers
from .serializers import TeachersSerializers
from rest_framework import generics
from django.shortcuts import render
from ipware import get_client_ip
from datetime import datetime
from user_agents import parse


# Create your views here.


class TeachersListView(generics.ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers


class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers


def my_view(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    client_ip = get_client_ip(request)
    request_time = datetime.now()
    user_agents_parse = parse(user_agent)
    device_full_name = user_agents_parse.device.family
    context = {
        'user_agent': user_agent,
        'client_ip': client_ip,
        'request_time': request_time,
        'device_full_name': device_full_name,
    }
    return render(request, 'my_template.html', context)