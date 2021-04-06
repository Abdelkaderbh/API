from rest_framework import serializers
from .models import rdv
from users.models import patient
 
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient
        fields = ('id','nom','prénom','naiss','téléphone') 
        
class rdv_serializer(serializers.ModelSerializer):
    patNom = serializers.CharField(source='patient.nom', read_only=True)
    class Meta:
        model=rdv
        fields='__all__'