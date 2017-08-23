# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    def __unicode__(self):
        return "{} - {}".format(self.id,self.username)


class Bebida(models.Model):

    nome = models.CharField(max_length=20,null=False,blank=False,unique=True)
    preco = models.FloatField()
    volume = models.FloatField()

    def __unicode__(self):
        return "{} - R${} - Garrafa em: {} ml".format(self.nome,self.preco,self.volume)

class Rack(models.Model):

    date = models.DateTimeField(auto_now=True)
    quantidade = models.ForeignKey('QuantidadeLitro')

    def __unicode__(self):
        return "{} - {}".format(self.id,self.date)

class Estoque(models.Model):

    bebida = models.OneToOneField('Bebida',null=False,blank=True,unique=True)
    quantidade = models.IntegerField()


    def __unicode__(self):
        return "Resta {} {}".format(self.quantidade,self.bebida.nome)


class QuantidadeCompra(models.Model):

    bebida = models.OneToOneField('Bebida',null=False,blank=True,unique=True)
    porcentagem = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem)

class QuantidadeLitro(QuantidadeCompra):

    m_litros = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem,self.m_litros)

class Compra(models.Model):

    usuario = models.ForeignKey(User,blank=False,null=False)
    quantidade = models.ForeignKey(QuantidadeCompra,blank=False,null=False)


    # reescrever o Save()
