# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-04 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppFarma', '0002_auto_20160803_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.IntegerField()),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellido', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=10)),
                ('Direccion', models.CharField(max_length=30)),
                ('Tipo', models.CharField(choices=[('U', 'usuario'), ('A', 'administrador'), ('E', 'empleado')], max_length=15)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
