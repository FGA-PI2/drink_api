# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from rest_framework import viewsets
from serializers import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    Simple View to render the User information json.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
