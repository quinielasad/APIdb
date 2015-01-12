# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField(max_length=64)),
                ('fecha_de_juego', models.DateTimeField(verbose_name=b'Fecha de Juego')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('local', models.TextField()),
                ('visitante', models.TextField()),
                ('is_pleno', models.BooleanField()),
                ('jornada', models.ForeignKey(to='principal.Jornada')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
