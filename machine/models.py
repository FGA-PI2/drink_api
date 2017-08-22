# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    def __unicode__(self):
        return "{} - {}".format(self.id,self.username)


class Bebida(models.Model):

    name = models.CharField(max_length=20,null=False,blank=False,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField(max_length=100)
    rack = models.ForeignKey('Bebida',null=True,related_name="bebidas")

    def __unicode__(self):
        return "{} - {}".format(self.name,self.price,self.quantity)

class Rack(models.Model):

    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} - {}".format(self.id,self.date)
