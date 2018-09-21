# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-21 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0011_auto_20180921_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='estado',
            field=models.CharField(choices=[('graduado', 'graduado'), ('egresado', 'egresado'), ('inscrito', 'inscrito'), ('plazo adicional', 'plazo adicional'), ('indeterminado', 'indeterminado'), ('baja temporal', 'baja temporal'), ('baja definitiva', 'baja definitiva')], default='vigente', max_length=15),
        ),
    ]
