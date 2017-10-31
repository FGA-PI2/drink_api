# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

from serializers import *
from rest_framework import viewsets,generics
from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from filters import *
from paypalrestsdk import Payment
from rest_framework import status


class PayPalView(APIView):



    def post(self, request,format=None):

        item_name = request.data['name']
        item_preco = request.data['price']
        buyer = request.data['user']

        payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute",
            "cancel_url": "http://localhost:8000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": item_name,
                    "sku": "item",
                    "price": item_preco,
                    "currency": "BRL",
                    "quantity": 1}]},
            "amount": {
                "total": item_preco,
                "currency": "BRL"},
            "description": "Compra de uma bebida feita no SunBar."}]})

        if payment.create():
            PayPal.objects.create(user=request.data['user'],payment_id=payment.id)
            response = Response({"paymentID": payment.id},status=status.HTTP_201_CREATED)
        else:
            data = payment.error
            response = Response(data,status=status.HTTP_400_BAD_REQUEST)

        return response


class PayPalExecute(APIView):

    def post(self,request,format=None):

        payer_id = request.data['payer_id']
        payment_id = request.data['payment_id']

        payment = Payment.find(payerID)

        if payment.execute({"payer_id": payer_id}):
            data = payment
            response = Response(data,status=status.HTTP_201_CREATED)
        else:
            data = payment.erro
            response = Response(data,status=status.HTTP_400_BAD_REQUEST)


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
    lookup_field = "nome"


class PedidoViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class CompraViewSet(viewsets.ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CompraFilter
    http_method_names = ['get','post','head']
