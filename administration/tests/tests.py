# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from administration.models import *
from authentication.models import User
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

class PedidoTest(APITestCase):

    factory = APIClient()

    def test_create_pedido(self):

        url = '/bebida/'
        data = {
            "nome": "Coca-Cola",
            "posicao": 2,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }
        response = self.factory.post(url,data,format='json')


        url = '/pedido/'
        data = {
            "bebida_name": 'Coca-Cola',
            "volume": 350,
            "compra": None
        }
        response = self.factory.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pedido.objects.count(),1)
        self.assertEqual(Pedido.objects.get().bebida.nome,'Coca-Cola')


##drink
class DrinkTest(APITestCase):

    factory = APIClient()


    def setUp(self):

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

        self.proporcao = [{
             "bebida": 'Coca-Cola',
             "volume": 100
         },
         {
             "bebida": 'Agua',
             "volume": 100
         },
         {
             "bebida": 'AguaGas',
             "volume": 100
         }]

        self.nome = "drink"
        self.descricao = 'uma bebida de teste'
        self.volume = 300

        self.data = {
             'proporcao': self.proporcao,
             'nome': self.nome,
             'descricao': self.descricao,
             'volume': self.volume
         }

        self.url = '/drink/'

    def test_create_drink(self):

        response = self.factory.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drink.objects.count(),1)
        self.assertEqual(Drink.objects.get().nome,'drink')

    def test_valor_drink(self):
        response = self.factory.post(self.url,self.data,format='json')
        retorno = self.client.get('/drink/')
        response.render()
        self.assertAlmostEqual(response.data['preco'],1.04,delta=0.1)


##Code

class CodeTest(APITestCase):

    def setUp(self):
        #Create user for code test
        self.factory = APIClient()

        User.objects.create(
            email= "teste@teste.com",
            creditos=9999,
            data_nascimento="1999-01-01",
            first_name="teste",
            password="123123"
        )

        self.data = {
            "is_valid": True,
            "qr_code": "https://testeqrcode.com",
            "usuario" : 1 #ForeignKey do user
        }

        self.url = '/code/'

    def test_create_code(self):
        response = self.factory.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QrCode.objects.count(),1)
        self.assertEqual(QrCode.objects.get().usuario.email,'teste@teste.com')
        self.assertEqual(QrCode.objects.get().is_valid,True)

##Compra

class CompraTest(APITestCase):


    def setUp(self):
        #Bebida
        Bebida.objects.create(
            nome = "Coca-Cola",
            posicao = 2,
            remaining_quantity = 2000,
            preco = 7,
            volume = 2000
        )

        #usuario
        User.objects.create(
            email= "teste@teste.com",
            creditos=9999,
            data_nascimento="1999-01-01",
            first_name="teste",
            password="123123"
        )

        #code
        QrCode.objects.create(
            is_valid = True,
            qr_code = "https://testeqrcode.com",
            usuario = User.objects.last()
        )

        #pedido
        Pedido.objects.create(
            bebida = Bebida.objects.last(),
            volume = 400
        )

        #infos sobre compra
        self.factory = APIClient()
        self.data = {
            "nome": "Pura Coca-Cola",
            "gelo": True,
            "preco": 14.0,
            "data_compra": "2017-11-07",
            "usuario": 8
        }
        self.url = '/compra/'


        def test_create_compra(self):
            response = self.factory.post(self.url,self.data,format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Compra.objects.count(),1)
            self.assertEqual(Compra.objects.get().usuario.email,'teste@teste.com')
            self.assertEqual(Compra.objects.get().nome,"Pura Coca-Cola")
