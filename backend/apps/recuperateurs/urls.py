from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecuperateurViewSet, AgrementViewSet, verifier_droit,
    specialisation_hierarchie, mes_types_dechets,
)

router = DefaultRouter()
router.register('agrements', AgrementViewSet, basename='agrement')
router.register('', RecuperateurViewSet, basename='recuperateur')

urlpatterns = [
    path('verifier-droit/', verifier_droit),
    path('specialisation-hierarchie/', specialisation_hierarchie),
    path('mes-types-dechets/', mes_types_dechets),
    path('', include(router.urls)),
]
