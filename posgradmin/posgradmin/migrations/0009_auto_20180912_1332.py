# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0008_auto_20180906_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academico',
            name='anexo_SNI',
        ),
        migrations.RemoveField(
            model_name='academico',
            name='anexo_estimulo',
        ),
    ]