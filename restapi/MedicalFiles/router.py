from rest_framework import routers
from .views import MedicalFiles_viewset


router=routers.DefaultRouter()
router.register('MedicalFiles',MedicalFiles_viewset)