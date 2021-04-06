from django.db import models
from users.models import patient

class MedicalFiles(models.Model):
    Patient = models.ForeignKey(patient,on_delete=models.SET_NULL, null=True)
    cancer_type=models.CharField(max_length=120)
    pdf_files = models.FileField()
    scanner_type = models.CharField(max_length=140)
    scanner_files = models.ImageField()