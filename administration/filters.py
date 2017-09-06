import django_filters
from rest_framework import filters
from models import *

class CompraFilter(filters.FilterSet):
    data_compra = django_filters.DateTimeFilter(name="data_compra", lookup_expr='exact')

    class Meta:
        model = Compra
        fields = ['data_compra','usuario__id']
