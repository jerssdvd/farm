# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-05 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFarma', '0004_auto_20160804_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='Tipo',
            field=models.CharField(choices=[('U', 'usuario'), ('A', 'administrador')], max_length=15),
        ),
    ]
