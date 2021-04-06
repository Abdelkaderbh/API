from django.db import models

class patient(models.Model): 
    nom = models.CharField(max_length=60)
    prénom=models.CharField(max_length=70)
    naiss=models.DateField(blank=True, null=True)
    sexe=models.CharField(max_length=20)
    etatCivil=models.CharField(max_length=50)
    profession=models.CharField(max_length=80)
    téléphone= models.IntegerField()
    adresse=models.TextField()
    email=models.EmailField()
    def __str__(self):
        return self.nom



class doctor(models.Model):
    D_nom = models.CharField(max_length=60)
    D_prénom=models.CharField(max_length=70)
    D_naiss=models.DateField(blank=True, null=True)
    spécialité = models.CharField(max_length=40)
    éducation = models.TextField(max_length=250)
    Diplôme = models.TextField(max_length=250)
    expérience_professionnelle=models.TextField(max_length=250)
    D_adresse=models.TextField()
    N_téléphone= models.IntegerField()
    D_email=models.EmailField()

    def __str__(self):
        return self.D_nom