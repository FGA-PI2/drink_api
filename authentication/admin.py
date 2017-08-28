# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from django.db.models.base import ModelBase
# Register your models here.

class UserAdmin(admin.ModelAdmin):
   search_fields = ('name',)




admin.site.register(User,UserAdmin)
