# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from authentication.models import User
from django.utils import timezone

class Bebida(models.Model):

    nome = models.CharField(max_length=20,null=False,blank=False,unique=True,primary_key=True)
    preco = models.FloatField()
    volume = models.FloatField()
    posicao = models.IntegerField()

    def __unicode__(self):
        return "{} - R${} - Garrafa de {} ml. Posicao {}".format(self.nome,self.preco,self.volume,self.posicao)

class Item(models.Model):

    bebida = models.ForeignKey('Bebida',null=False,blank=True)
    volume = models.IntegerField()


    def __unicode__(self):
        return "{} {}".format(self.bebida.nome,self.porcentagem)


class Pedido(Item):

    compra = models.ForeignKey('Compra',blank=True,null=True,related_name="pedido")

    def __unicode__(self):
        return "A Mistura foi {} - {} na compra: {}".format(self.bebida,self.porcentagem,self.compra.id)


class ItemDrink(Item):

    drink = models.ForeignKey('Drink',blank=True,related_name="proporcao")

    def __unicode__(self):
        return "{}:{}".format(self.bebida,self.porcentagem)

class Drink(models.Model):

    nome = models.CharField(max_length=40,unique=True,primary_key=True,default="")
    descricao = models.CharField(max_length=50)
    volume = models.FloatField()
    preco = models.FloatField(default=0)

    def __unicode__(self):
        return "{}".format(self.nome)

class QuantidadeLitro(Item):

    m_litros_atual = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem,self.m_litros_atual)

class Compra(models.Model):

    nome = models.CharField(max_length=40,default="custom")
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,null=False)
    qr_code = models.ForeignKey('QrCode',null=True)
    gelo = models.BooleanField(default=False)
    preco = models.FloatField(default=0)
    data_compra = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "{} - {} ".format(self.usuario.name,self.pedido)


class QrCode(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_valid = models.BooleanField(default=False)
    qr_code = models.CharField(max_length=200)

    def __unicode__(self):
        return "{} - {}".format(self.compra.usuario.name,self.is_valid)

class Cardapio(models.Model):

    data = models.DateTimeField(auto_now_add=True)
    drinks = models.ManyToManyField(Drink,related_name="cardapios")

    def __unicode__(self):
        return "Cardapio oferecido dia {}/{} as {}:{}".format(self.data.day,self.data.month,self.data.hour,self.data.minute)
