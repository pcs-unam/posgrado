# Generated by Django 3.2.15 on 2023-03-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0117_auto_20230305_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apoyomovilidad',
            options={'verbose_name_plural': 'Apoyos para Movilidad'},
        ),
        migrations.RenameField(
            model_name='apoyomovilidad',
            old_name='tipo',
            new_name='tipo_actividad',
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='ciudad',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='internacional',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='pais',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='semestre',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2)], default=1, verbose_name='semestre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='tipo_apoyo',
            field=models.CharField(choices=[('paep', 'PAEP'), ('larga duración', 'Larga Duración'), ('otro', 'otro')], default='paep', max_length=255),
        ),
        migrations.AddField(
            model_name='apoyomovilidad',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='año'),
        ),
        migrations.AlterField(
            model_name='apoyomovilidad',
            name='estado',
            field=models.CharField(choices=[('solicitado', 'solicitado'), ('reporte entregado', 'reporte entregado'), ('cancelado', 'cancelado')], default='solicitado', max_length=25),
        ),
    ]
