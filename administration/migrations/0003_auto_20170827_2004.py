# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20170827_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='cardapio',
        ),
        migrations.AddField(
            model_name='cardapio',
            name='drinks',
            field=models.ManyToManyField(related_name='cardapios', to='administration.Drink'),
        ),
    ]
