from .models import Listeners
from rest_framework import serializers


class ListenersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listeners
        fields = ('id', 'full_name', 'photo', 'description')