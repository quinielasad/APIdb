# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0004_auto_20150109_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApuestaPartido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(default=b'0', max_length=12, choices=[(b'1', b'1'), (b'X', b'X'), (b'2', b'2')])),
                ('partido', models.ForeignKey(to='principal.Partido')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntuacion', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='partido',
            old_name='is_pleno',
            new_name='isPleno',
        ),
        migrations.AddField(
            model_name='partido',
            name='doscomun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='golLocal',
            field=models.CharField(max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='golVisitante',
            field=models.CharField(max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.CharField(default=b'0', max_length=12, choices=[(b'0', b'0'), (b'1', b'1'), (b'X', b'X'), (b'2', b'2')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='resultadoLocal',
            field=models.CharField(max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='resultadoVisitante',
            field=models.CharField(max_length=12, null=True, choices=[(b'0', b'0'), (b'1', b'1'), (b'2', b'2'), (b'M', b'M')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='unoComun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='xComun',
            field=models.DecimalField(default=0.0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]
