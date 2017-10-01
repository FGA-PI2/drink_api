import django_filters
from rest_framework import filters
from models import *
from django.db import models as django_models

class CompraFilter(filters.FilterSet):

    class Meta:
        model = Compra
        fields = {
            'data_compra': ['exact'],
            'usuario__id': ['exact']
            }
