# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20150112_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='doscomun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='golLocal',
            field=models.CharField(blank=True, max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='golVisitante',
            field=models.CharField(blank=True, max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultado',
            field=models.CharField(default=b'0', max_length=12, blank=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'X', b'X'), (b'2', b'2')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultadoLocal',
            field=models.CharField(blank=True, max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultadoVisitante',
            field=models.CharField(blank=True, max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='unoComun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partido',
            name='xComun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
