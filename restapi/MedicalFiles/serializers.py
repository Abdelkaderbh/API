from rest_framework import serializers
from .models import MedicalFiles
from users.models import patient

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient
        fields = '__all__' 
class MedicalFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalFiles
        fields ='__all__'