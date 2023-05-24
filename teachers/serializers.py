from .models import Teachers
from  rest_framework import serializers


class TeachersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'full_name', 'education', 'academic_title','specialty', 'photo', 'description')