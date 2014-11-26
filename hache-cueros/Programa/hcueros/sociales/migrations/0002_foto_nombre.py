# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sociales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='nombre',
            field=models.CharField(default=datetime.date(2014, 11, 25), max_length=200),
            preserve_default=False,
        ),
    ]
