# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sociales', '0003_auto_20141125_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen',
            field=models.ImageField(upload_to=b'FotosSociales', null=True, verbose_name=b'Fotos'),
        ),
    ]
