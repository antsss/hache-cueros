# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('tipo_social', models.CharField(max_length=1)),
                ('pub_ini_date', models.DateTimeField(verbose_name=b'fecha publicado')),
                ('pub_fin_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
