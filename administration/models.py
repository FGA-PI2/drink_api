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


class Pedido(models.Model):

    bebida = models.ForeignKey('Bebida',null=False,blank=True)
    porcentagem = models.FloatField()
    compra = models.ForeignKey('Compra',blank=True,null=True,related_name="pedido")

    def __unicode__(self):
        return "{} {}".format(self.bebida.nome,self.porcentagem)

class QuantidadeLitro(Pedido):

    m_litros = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem,self.m_litros)

class Compra(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,null=False)

    def __unicode__(self):
        return "{} - {} ".format(self.usuario.name,self.pedido)
