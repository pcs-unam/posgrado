# Generated by Django 3.2.15 on 2023-05-02 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posgradmin', '0136_invitado_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='observaciones',
            new_name='observaciones_profesores',
        ),
    ]
