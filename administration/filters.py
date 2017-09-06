import django_filters
from rest_framework import filters

class CompraFilter(filters.FilterSet):
    data_compra = django_filters.DateTimeFilter(name="data_compra", lookup_expr='gte')

    class Meta:
        model = Event
        fields = ['data_compra','usuario__id']
