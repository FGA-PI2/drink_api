# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from models import *
# Create your tests here.




#testes para provar que consegue instanciar os objetos.


## bebidas

class BebidaTest(APITestCase):

    factory = APIClient()

    def test_create_bebida(self):

        url = '/bebida/'
        data = {
            "nome": "Coca-Cola",
            "posicao": 2,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }
        response = self.factory.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bebida.objects.count(),1)
        self.assertEqual(Bebida.objects.get().nome,'Coca-Cola')



##Pedido

##drink

##Code




##Compra

"""
{
        "id": 53,
        "pedido": [
            {
                "id": 116,
                "bebida": {
                    "nome": "Rum",
                    "posicao": 2,
                    "remaining_quantity": 96820.0,
                    "preco": 35.0,
                    "volume": 1000.0
                },
                "bebida_name": "Rum",
                "volume": 400,
                "compra": 53
            }
        ],
        "qr_code": {
            "id": 53,
            "is_valid": false,
            "qr_code": "https://chart.googleapis.com/chart?chs=500x500&cht=qr&chl={\"usuario\":\"8\",\"data_compra\":\"2017-11-07T15:46:26.649Z\"}",
            "usuario": 8
        },
        "nome": "Puro Rum",
        "gelo": true,
        "preco": 14.0,
        "data_compra": "2017-11-07T15:46:26.649000Z",
        "usuario": 8
    },
"""


#Testes de validacao


## Validar se o numero de bebidas maximo e respeitado



##validar o volume maximo de um drink/compra


##Validar CODE com dados corretos
