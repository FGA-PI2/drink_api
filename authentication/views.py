# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from rest_framework import viewsets,generics
import django_filters.rest_framework
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserViewList(viewsets.ModelViewSet):
    """
    Simple View to render the User information json.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('email',)
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
