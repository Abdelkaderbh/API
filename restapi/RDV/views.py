from django.shortcuts import render
from rest_framework import viewsets
from .serializers import rdv_serializer
from .models import rdv


class rdv_viewset(viewsets.ModelViewSet):
    queryset=rdv.objects.all()
    serializer_class=rdv_serializer
