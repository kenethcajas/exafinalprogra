# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('articulo1', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('marca1', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('DPIcliente', models.CharField(max_length=30)),
                ('cantidad', models.CharField(max_length=30)),
                ('articulo', models.ForeignKey(to='ventasfinal.Articulo')),
                ('marca', models.ForeignKey(to='ventasfinal.Marca')),
            ],
        ),
    ]
