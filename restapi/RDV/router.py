from rest_framework import routers
from .views import rdv_viewset


router=routers.DefaultRouter()
router.register('rdv',rdv_viewset)