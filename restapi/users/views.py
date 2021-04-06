from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import patient_serializer , doctor_serializer

from .models import  patient,doctor


class patient_viewset(viewsets.ModelViewSet):
    queryset=patient.objects.all()
    serializer_class=patient_serializer
    

class doctor_viewset(viewsets.ModelViewSet):
    queryset=doctor.objects.all()
    serializer_class=doctor_serializer
