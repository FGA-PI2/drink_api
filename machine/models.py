# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from managers import UserManager

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class User(AbstractBaseUser):

    email = models.EmailField(unique=True)
    creditos = models.FloatField(default=0)
    data_nascimento = models.DateField()
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return "{} - {} - {}".format(self.id,self.email,self.creditos)


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

    bebida = models.ForeignKey('Bebida',null=False,blank=True)
    porcentagem = models.FloatField()
    compra = models.ForeignKey('Compra',blank=True,null=True,related_name="pedido")

    def __unicode__(self):
        return "{} {}".format(self.bebida.nome,self.porcentagem)

class QuantidadeLitro(QuantidadeCompra):

    m_litros = models.FloatField()

    def __unicode__(self):
        return "{} {} {}".format(self.bebida.name,self.porcentagem,self.m_litros)

class Compra(models.Model):

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,null=False)
    # pedido = models.ForeignKey(QuantidadeCompra,blank=False,null=False)

    def __unicode__(self):
        return "{} - {} ".format(self.usuario.name,self.pedido)
