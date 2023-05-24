from rest_framework import serializers
from .models import InactiveStudents, ActiveStudents


class InActiveStudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = InactiveStudents
        fields = ('id', 'full_name', 'study_group', 'photo', 'description')


class ActiveStudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActiveStudents
        fields = ('id', 'full_name', 'study_group', 'photo', 'description')
