# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from authentication.models import User

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


class Item(models.Model):

    bebida = models.ForeignKey('Bebida',null=False,blank=True)
    porcentagem = models.FloatField()


    def __unicode__(self):
        return "{} {}".format(self.bebida.nome,self.porcentagem)


class Pedido(Item):

    compra = models.ForeignKey('Compra',blank=True,null=True,related_name="pedido")

    def __unicode__(self):
        return "A Mistura foi {} - {} na compra: {}".format(self.bebida,self.porcentagem,self.compra.id)


class ItemDrink(Item):

    drink = models.ForeignKey('Drink',blank=True,related_name="proporcao")

    def __unicode__(self):
        return "{}:{} - drink: {}".format(self.bebida,self.porcentagem)

class Drink(models.Model):

    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=50)
    volume = models.FloatField()


    def __unicode__(self):
        return "{}".format(self.nome)

class QuantidadeLitro(Item):

    m_litros_atual = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem,self.m_litros_atual)

class Compra(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,null=False)
    qr_code = models.ForeignKey('QrCode',null=True)

    def __unicode__(self):
        return "{} - {} ".format(self.usuario.name,self.pedido)


class QrCode(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_valid = models.BooleanField(default=False)
    qr_code = models.URLField(max_length=200)

    def __unicode__(self):
        return "{} - {}".format(self.compra.usuario.name,self.is_valid)

class Cardapio(models.Model):

    data = models.DateTimeField(auto_now_add=True)
    drinks = models.ManyToManyField(Drink,related_name="cardapios")

    def __unicode__(self):
        return "Cardapio oferecido dia {}/{} as {}:{}".format(self.data.day,self.data.month,self.data.hour,self.data.minute)
