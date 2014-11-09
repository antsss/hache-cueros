# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sociales', '0002_auto_20141109_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='pub_fin_date',
        ),
        migrations.RemoveField(
            model_name='social',
            name='pub_ini_date',
        ),
    ]
