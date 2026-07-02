from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BCViewSet, generate_bc, generate_bc_word

router = DefaultRouter()
router.register(r'', BCViewSet, basename='bc')

urlpatterns = [
    path('generate-bc/',      generate_bc,      name='generate-bc'),
    path('generate-bc-word/', generate_bc_word, name='generate-bc-word'),
    path('', include(router.urls)),
]
