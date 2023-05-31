from .models import LearningProcess
from rest_framework import serializers


class LearningProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProcess
        fields = ('id', 'title', 'body', "image")
