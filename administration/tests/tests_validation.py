from  __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from administration.models import *
from authentication.models import User

class TestMaxBebida(TestCase):

    def setUp(self):
        #criar 3 bebidas em diferentes posicoes
        Bebida.objects.create(
            nome = "Coca-Cola",
            posicao = 1,
            remaining_quantity = 2000,
            preco = 7,
            volume = 2000
        )

        Bebida.objects.create(
            nome = "Agua",
            posicao = 2,
            remaining_quantity = 2000,
            preco = 7,
            volume = 2000
        )

        Bebida.objects.create(
            nome = "AguaGas",
            posicao = 3,
            remaining_quantity = 2000,
            preco = 7,
            volume = 2000
        )

        self.url = '/bebida/'
        self.factory = APIClient()
        self.data = {
            "nome": "FailTest",
            "posicao": 4,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }

    def test_posicao_4_bebida(self):
        response = self.factory.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Bebida.objects.count(),3)
