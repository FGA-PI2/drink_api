# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    Simple View to render the User information json.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'


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

class QuantidadeCompraViewSet(viewsets.ModelViewSet):

    queryset = QuantidadeCompra.objects.all()
    serializer_class = QuantidadeCompraSerializer

class CompraViewSet(viewsets.ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
