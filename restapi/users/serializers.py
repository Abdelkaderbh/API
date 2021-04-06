from rest_framework import serializers
from .models import  patient , doctor


class patient_serializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields='__all__'

class doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model=doctor
        fields='__all__'