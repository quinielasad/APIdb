# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150108_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jornada',
            old_name='Fecha de Juego',
            new_name='fechadejuego',
        ),
    ]
