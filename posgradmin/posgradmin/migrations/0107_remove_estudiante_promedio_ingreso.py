# Generated by Django 3.2.13 on 2022-09-17 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0106_estudiante_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='promedio_ingreso',
        ),
    ]
