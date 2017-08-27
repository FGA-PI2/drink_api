# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
                ('preco', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=50)),
                ('quantidade', models.FloatField()),
                ('cardapio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='administration.Cardapio')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('bebida', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Bebida')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentagem', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=False)),
                ('qr_code', models.URLField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDrink',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.Item')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proporcao', to='administration.Drink')),
            ],
            bases=('administration.item',),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.Item')),
                ('compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='administration.Compra')),
            ],
            bases=('administration.item',),
        ),
        migrations.CreateModel(
            name='QuantidadeLitro',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administration.Item')),
                ('m_litros_atual', models.FloatField()),
            ],
            bases=('administration.item',),
        ),
        migrations.AddField(
            model_name='item',
            name='bebida',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='administration.Bebida'),
        ),
        migrations.AddField(
            model_name='rack',
            name='quantidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.QuantidadeLitro'),
        ),
    ]
