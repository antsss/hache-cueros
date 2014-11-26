# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sociales', '0002_foto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
