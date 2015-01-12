# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jornada',
            name='fecha_de_juego',
        ),
        migrations.AddField(
            model_name='jornada',
            name='Fecha de Juego',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
