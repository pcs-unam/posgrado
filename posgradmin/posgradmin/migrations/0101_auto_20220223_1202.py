# Generated by Django 3.0.6 on 2022-02-23 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0100_auto_20220223_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='campo_conocimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.CampoConocimiento'),
        ),
        migrations.AddField(
            model_name='historial',
            name='lineas_investigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.LineaInvestigacion'),
        ),
    ]