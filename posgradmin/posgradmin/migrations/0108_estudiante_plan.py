# Generated by Django 3.2.13 on 2022-09-17 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0107_remove_estudiante_promedio_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='plan',
            field=models.CharField(choices=[('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], default='Maestría', max_length=20),
        ),
    ]
