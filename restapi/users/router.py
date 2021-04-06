from  rest_framework import routers
from .views import patient_viewset,doctor_viewset
from RDV.views import rdv_viewset
from MedicalFiles.views import  MedicalFiles_viewset



router=routers.DefaultRouter()
router.register('patient',patient_viewset)
router.register('doctor',doctor_viewset)
router.register('RendezVous',rdv_viewset)
router.register('MedicalFiles',MedicalFiles_viewset)