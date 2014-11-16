# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_auto_20141112_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='precio_miprueba',
            new_name='precio_ma',
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_mi',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
