# Generated by Django 3.0.3 on 2020-02-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0055_auto_20200215_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academico',
            name='fecha_acreditacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='academico',
            name='ultima_reacreditacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
