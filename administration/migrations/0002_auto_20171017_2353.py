# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='posicao',
            field=models.IntegerField(unique=True),
        ),
    ]
