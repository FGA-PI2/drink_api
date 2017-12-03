# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from models import User
# Create your tests here.



class UserTest(APITestCase):

    def setUp(self):
        self.url = '/users/'
        self.data = {
            "email": "teste@teste.com",
            "is_superuser": False,
            "creditos": 9999,
            "data_nascimento": '1999-01-01',
            "password": "123123",
            "first_name": "teste"
        }

        self.factory = APIClient()

    def test_create_user(self):
        response = self.factory.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(User.objects.get().email,'teste@teste.com')
