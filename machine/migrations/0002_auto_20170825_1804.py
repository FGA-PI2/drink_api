# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantidadecompra',
            name='bebida',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='machine.Bebida'),
        ),
    ]
