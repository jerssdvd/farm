# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-15 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFarma', '0006_auto_20160807_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='CodCompra',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='factura',
            name='NumF',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='farmaceutico',
            name='CodigoF',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='producto',
            name='Cod',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Codigo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Codigo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='venta',
            name='Code',
            field=models.CharField(max_length=30),
        ),
    ]