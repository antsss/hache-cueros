# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('publicada', models.BooleanField(default=False)),
                ('articulos', models.ManyToManyField(to='articulos.Articulo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precio_miprueba',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='publicado_ma',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='publicado_mi',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
