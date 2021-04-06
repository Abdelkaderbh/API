from django.db import models
from users.models import patient



class rdv(models.Model):
    patient=models.ForeignKey(patient,on_delete=models.SET_NULL, null=True)
    date_rdv=models.DateTimeField()
