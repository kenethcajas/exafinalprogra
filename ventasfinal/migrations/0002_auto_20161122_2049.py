# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventasfinal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marca',
            new_name='Usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='marca1',
            new_name='usuario1',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='marca',
            new_name='usuario',
        ),
    ]
