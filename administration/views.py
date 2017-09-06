# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

from serializers import *
from rest_framework import viewsets,generics
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from filters import *
# Create your views here.

class CardapioViewSet(viewsets.ModelViewSet):

    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer

class DrinkViewSet(viewsets.ModelViewSet):

    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class QrCodeViewSet(viewsets.ModelViewSet):

    queryset = QrCode.objects.filter(is_valid=True)
    serializer_class = QrCodeSerializer

class BebidasViewSet(viewsets.ModelViewSet):
    """
    Viewset to return bebidas information.
    """

    queryset = Bebida.objects.all()
    serializer_class = BebidasSerializer
    lookup_field = "name"

class RackViewSet(viewsets.ModelViewSet):
    """
    ViewSet to return the information about racks.
    """

    queryset = Rack.objects.all()
    serializer_class = RackSerializer

class EstoqueViewSet(viewsets.ModelViewSet):

    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class PedidoViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class CompraViewSet(viewsets.ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # filter_fields = ('usuario__id','data_compra')
    filter_class = EventFilter
