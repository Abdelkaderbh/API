from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MedicalFilesSerializer
from .models import MedicalFiles

class MedicalFiles_viewset(viewsets.ModelViewSet):
    queryset=MedicalFiles.objects.all()
    serializer_class = MedicalFilesSerializer