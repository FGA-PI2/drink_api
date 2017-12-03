# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from models import *
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


    def test_create_drink(self):
        """
        Esse teste precisa verificar a criacao de um drink.

        para um drink sao criados 3 instancias de 'proporcao'.
        """


        #criar 3 bebidas
        url = '/bebida/'

        bebida1 = {
            "nome": "Coca-Cola",
            "posicao": 1,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }

        bebida2 = {
            "nome": "Agua",
            "posicao": 2,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }

        bebida3 = {
            "nome": "AguaGas",
            "posicao": 3,
            "remaining_quantity": 2000,
            "preco": 7,
            "volume": 2000
        }

        self.factory.post(url,bebida1,format='json')
        self.factory.post(url,bebida2,format='json')
        self.factory.post(url,bebida3,format='json')



        url = '/drink/'


        nome = "drink"
        descricao = 'uma bebida de teste'
        volume = 300
        proporcao = [{
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

        data = {
            'proporcao': proporcao,
            'nome': nome,
            'descricao': descricao,
            'volume': volume
        }

        response = self.factory.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drink.objects.count(),1)
        self.assertEqual(Drink.objects.get().nome,'drink')


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



#Testes de validacao


## Validar se o numero de bebidas maximo e respeitado



##validar o volume maximo de um drink/compra


##Validar CODE com dados corretos
