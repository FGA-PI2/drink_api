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

# Create your models here.



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class User(AbstractBaseUser):

    id = models.BigIntegerField(primary_key = True)
    email = models.EmailField(unique=True)
    creditos = models.FloatField(default=0)
    data_nascimento = models.DateField()
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30,blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return "{} - {}".format(self.email,self.creditos)
