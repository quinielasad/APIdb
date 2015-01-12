# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20150108_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='nombre',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='is_pleno',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='local',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='visitante',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
    ]
