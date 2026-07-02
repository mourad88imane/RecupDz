from rest_framework import serializers
from .models import BonCommande


class BCSerializer(serializers.ModelSerializer):
    statut_display   = serializers.CharField(source='get_statut_display', read_only=True)
    recuperateur_nom = serializers.CharField(source='recuperateur.nom_raison_sociale', read_only=True)

    class Meta:
        model  = BonCommande
        fields = '__all__'
