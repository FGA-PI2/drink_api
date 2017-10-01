# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *
from django.db.models.base import ModelBase




class BebidaAdmin(admin.ModelAdmin):
   fields = ('nome','preco','volume')
   search_fields = ('nome','preco')

admin.site.register(Bebida,BebidaAdmin)
