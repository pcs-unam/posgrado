# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-20 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0030_auto_20190620_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]