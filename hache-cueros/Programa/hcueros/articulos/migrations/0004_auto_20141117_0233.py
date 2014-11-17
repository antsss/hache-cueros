# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_auto_20141112_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='precio_ma',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio_mi',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
