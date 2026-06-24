import django_filters
from .models import Traceability

class TraceabilityFilter(django_filters.FilterSet):
    # Date précise (jour exact)
    date_recuperation = django_filters.DateFilter(field_name='date_recuperation', lookup_expr='exact')
    # Intervalle de dates
    date_min = django_filters.DateFilter(field_name='date_recuperation', lookup_expr='gte')
    date_max = django_filters.DateFilter(field_name='date_recuperation', lookup_expr='lte')
    # Statistiques mensuelles / annuelles
    mois  = django_filters.NumberFilter(field_name='date_recuperation', lookup_expr='month')
    annee = django_filters.NumberFilter(field_name='date_recuperation', lookup_expr='year')

    class Meta:
        model  = Traceability
        fields = ['recuperateur', 'statut', 'classe_dechet', 'destination_type',
                  'date_recuperation', 'date_min', 'date_max', 'mois', 'annee']
