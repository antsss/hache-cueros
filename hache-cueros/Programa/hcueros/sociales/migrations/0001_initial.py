# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'FotosSociales', verbose_name=b'Fotos')),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Fotos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('tipo_social', models.CharField(default=b'N', max_length=1, choices=[(b'F', b'Filosofia'), (b'N', b'Noticia')])),
                ('fecha_inicio_publicacion', models.DateField()),
                ('fecha_fin_publicacion', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Sociales',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='foto',
            name='social',
            field=models.ForeignKey(to='sociales.Social'),
            preserve_default=True,
        ),
    ]
