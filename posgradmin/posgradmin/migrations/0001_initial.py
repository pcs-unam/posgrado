# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posgradmin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_PRIDE', models.CharField(choices=[(b'sin PRIDE', b'sin PRIDE'), (b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D')], max_length=15)),
                ('nivel_SNI', models.CharField(choices=[(b'sin SNI', b'sin SNI'), (b'I', b'I'), (b'II', b'II'), (b'III', b'III'), (b'C', b'C'), (b'E', b'E')], max_length=15)),
                ('CVU', models.CharField(blank=True, max_length=100, null=True)),
                ('DGEE', models.CharField(blank=True, max_length=6, null=True)),
                ('numero_trabajador_unam', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'N\xc3\xbamero de trabajador (UNAM)')),
                ('tutor', models.BooleanField(default=False)),
                ('comite_academico', models.BooleanField(default=False)),
                ('fecha_acreditacion', models.DateField(blank=True, null=True)),
                ('acreditacion', models.CharField(choices=[(b'no acreditado', b'no acreditado'), (b'E', b'E'), (b'D', b'D'), (b'PD', b'PD'), (b'NPD', b'NPD'), (b'M', b'M'), (b'NPM', b'NPM'), (b'PM', b'PM')], max_length=15)),
                ('tesis_licenciatura', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Licenciatura')),
                ('tesis_licenciatura_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Licenciatura en los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('tesis_maestria', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Maestr\xc3\xada')),
                ('tesis_maestria_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Maestr\xc3\xada en los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('tesis_doctorado', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Doctorado')),
                ('tesis_doctorado_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de tesis dirigidas a nivel Doctorado en los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('participacion_comite_maestria', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de participaciones como miembro de comit\xc3\xa9 tutor en el PCS a nivel maestr\xc3\xada')),
                ('participacion_comite_doctorado', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de participaciones como miembro de comit\xc3\xa9 tutor en el PCS a nivel doctorado')),
                ('participacion_tutor_maestria', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de participaciones como tutor principal en el PCS a nivel maestr\xc3\xada')),
                ('participacion_tutor_doctorado', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de participaciones como tutor principal en el PCS a nivel doctorado')),
                ('tutor_principal_otros_programas', models.TextField(blank=True, verbose_name=b'Otros programas en los que participa como tutor principal')),
                ('tutor_otros_programas', models.TextField(blank=True, verbose_name=b'Otros programas en los que participa como miembro de comit\xc3\xa9 tutor')),
                ('articulos_internacionales', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de art\xc3\xadculos publicados en revistas internacionales')),
                ('articulos_internacionales_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de art\xc3\xadculos publicados en revistas internacionales durante los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('articulos_nacionales', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de art\xc3\xadculos publicados en revistas nacionales')),
                ('articulos_nacionales_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de art\xc3\xadculos publicados en revistas nacionales durante los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('libros', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de libros publicados')),
                ('libros_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de libros publicados durante los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('capitulos', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de cap\xc3\xadtulos de libro publicados')),
                ('capitulos_5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Cantidad de cap\xc3\xadtulos de libro publicados durante los \xc3\xbaltimos 5 a\xc3\xb1os')),
                ('lineas', models.TextField(blank=True, verbose_name=b'Temas de inter\xc3\xa9s y/o experiencia en ciencias de la sostenibilidad')),
                ('palabras_clave', models.TextField(blank=True, verbose_name=b'Palabras clave de temas de inter\xc3\xa9s y/o experienciaen ciencias de la sostenibilidad separadas por comas')),
                ('motivacion', models.TextField(blank=True, verbose_name=b'Motivaci\xc3\xb3n para participar en el Programa')),
                ('proyectos_sostenibilidad', models.TextField(blank=True, verbose_name=b'Principales proyectos relacionados con ciencias de la sostenibilidad durante los \xc3\xbaltimos cinco a\xc3\xb1os')),
                ('proyectos_vigentes', models.TextField(blank=True, verbose_name=b'Proyectos vigentes en los que pueden participar alumnos del PCS. Incluya fechas de terminaci\xc3\xb3n.')),
                ('disponible_tutor', models.BooleanField(default=False, verbose_name=b'Disponible como tutor principal (direcci\xc3\xb3n de alumnos)')),
                ('disponible_miembro', models.BooleanField(default=False, verbose_name=b'Disponible como miembro de comit\xc3\xa9 tutor (asesor\xc3\xada de alumnos)')),
                ('observaciones', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Acad\xe9micos',
            },
        ),
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acuerdos', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Acuerdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to=b'')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asociacion_PCS', models.BooleanField(default=False, verbose_name=b's\xc3\xb3lo para asociaci\xc3\xb3n con el PCS')),
            ],
        ),
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('archivo', models.FileField(upload_to=posgradmin.models.anexo_path)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnexoAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('archivo', models.FileField(upload_to=posgradmin.models.anexo_path)),
                ('academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Academico')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asistente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Asistentes de Proceso',
            },
        ),
        migrations.CreateModel(
            name='Beca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CampoConocimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'campos de conocimiento',
            },
        ),
        migrations.CreateModel(
            name='Catedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2)])),
                ('year', models.PositiveSmallIntegerField(verbose_name=b'A\xc3\xb1o')),
                ('sede', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'verbose_name_plural': 'C\xe1tedras',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.CharField(max_length=300)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[(b'tutoral', b'tutoral'), (b'candidatura', b'candidatura'), (b'grado', b'grado')], max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Comit\xe9s',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.CharField(max_length=100)),
                ('clave', models.CharField(blank=True, max_length=100, null=True)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('horas_semestre', models.PositiveSmallIntegerField(verbose_name=b'Horas por semestre')),
                ('tipo', models.CharField(choices=[(b'Obligatoria', b'Obligatoria'), ('Obligatorias de elecci\xf3n', 'Obligatorias de elecci\xf3n'), (b'Optativa', b'Optativa'), (b'Optativa, intersemestral', b'Optativa, intersemestral')], max_length=40)),
                ('programa', models.FileField(upload_to=posgradmin.models.curso_path, verbose_name=b'Documento con descripci\xc3\xb3n extensa.')),
            ],
        ),
        migrations.CreateModel(
            name='Dictamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolucion', models.CharField(choices=[(b'concedida', b'concedida'), (b'denegada', b'denegada')], max_length=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Dict\xe1menes',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=100)),
                ('ingreso', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'a\xc3\xb1o de ingreso al posgrado')),
                ('semestre', models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2)], null=True, verbose_name=b'semestre de ingreso al posgrado')),
                ('convenio', models.CharField(blank=True, max_length=100)),
                ('plan', models.CharField(choices=[('Maestr\xeda', 'Maestr\xeda'), ('Doctorado', 'Doctorado'), ('Doctorado directo', 'Doctorado directo'), ('Opci\xf3n a titulaci\xf3n', 'Opci\xf3n a titulaci\xf3n')], max_length=20)),
                ('estado', models.CharField(choices=[('graduado', 'graduado'), ('egresado', 'egresado'), ('vigente', 'vigente'), ('baja temporal', 'baja temporal'), ('baja definitiva', 'baja definitiva')], default='vigente', max_length=15)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('motivo_baja', models.CharField(blank=True, max_length=200)),
                ('fecha_titulacion', models.DateField(blank=True, null=True)),
                ('folio_titulacion', models.CharField(blank=True, max_length=200)),
                ('mencion_honorifica', models.BooleanField(default=False)),
                ('medalla_alfonso_caso', models.BooleanField(default=False)),
                ('semestre_graduacion', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradoAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[(b'licenciatura', b'licenciatura'), (b'maestria', b'maestria'), (b'doctorado', b'doctorado')], max_length=15)),
                ('grado_obtenido', models.CharField(max_length=100)),
                ('fecha_obtencion', models.DateField(verbose_name=b'Fecha de obtenci\xc3\xb3n de grado')),
                ('documento', models.FileField(upload_to=posgradmin.models.grado_path, verbose_name=b'Copia de documento probatorio')),
            ],
            options={
                'verbose_name_plural': 'Grados acad\xe9micos',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name=b'Instituci\xc3\xb3n u Organizaci\xc3\xb3n')),
                ('suborganizacion', models.CharField(max_length=150, verbose_name=b'Dependencia, Entidad o Departamento')),
                ('pais', models.CharField(blank=True, max_length=100, verbose_name=b'Pa\xc3\xads')),
                ('estado', models.CharField(blank=True, max_length=100)),
                ('dependencia_UNAM', models.BooleanField(default=False)),
                ('entidad_PCS', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'instituciones',
            },
        ),
        migrations.CreateModel(
            name='LineaInvestigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'l\xedneas de investigaci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=15, verbose_name=b'Grado acad\xc3\xa9mico (e.g. Dr., Lic.)')),
                ('curp', models.CharField(max_length=100, verbose_name=b'CURP, en caso de ser extranjero(a) ingresar la palabra extranjero(a)')),
                ('rfc', models.CharField(max_length=100, verbose_name=b'RFC, en caso de ser extranjero(a) ingresar la palabra extranjero(a)')),
                ('telefono', models.CharField(max_length=100)),
                ('telefono_movil', models.CharField(blank=True, max_length=100)),
                ('direccion1', models.CharField(max_length=150, verbose_name=b'direcci\xc3\xb3n del lugar de trabajo')),
                ('codigo_postal', models.PositiveSmallIntegerField(default=0)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('pasaporte', models.CharField(blank=True, max_length=200)),
                ('estado_civil', models.CharField(blank=True, max_length=200)),
                ('genero', models.CharField(choices=[(b'M', b'masculino'), (b'F', b'femenino')], max_length=1)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name=b'fecha de nacimiento')),
                ('headshot', models.ImageField(blank=True, null=True, upload_to=posgradmin.models.headshot_path, verbose_name=b'fotograf\xc3\xada')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('aprobado', models.BooleanField(default=False)),
                ('campo_conocimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.CampoConocimiento')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(default=b'sesi\xc3\xb3n ordinaria', max_length=100)),
                ('minuta', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Sesiones',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumen', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[(b'registrar_catedra', b'Registrar C\xc3\xa1tedra'), (b'solicitar_apoyo_economico', b'Solicitar Apoyo Econ\xc3\xb3mico'), (b'registrar_catedra', b'Registrar C\xc3\xa1tedra'), (b'solicitar_apoyo_economico', b'Solicitar Apoyo Econ\xc3\xb3mico'), (b'solicitar_baja_tutor', b'Solicitar Baja de Tutor\xc3\xada en el Programa'), (b'avisar_ausencia', b'Aviso de Ausencia por Sab\xc3\xa1tico u Otra Raz\xc3\xb3n'), (b'otro', b'Otro')], max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.CharField(choices=[(b'nueva', b'nueva'), (b'agendada', b'agendada'), (b'atendida', b'atendida'), (b'cancelada', b'cancelada')], default=b'nueva', max_length=30)),
                ('sesion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Sesion')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes',
            },
        ),
        migrations.AddField(
            model_name='proyecto',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='gradoacademico',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Institucion'),
        ),
        migrations.AddField(
            model_name='gradoacademico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Institucion'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dictamen',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='comite',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Estudiante'),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembro1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miembro1_comites', to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembro2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miembro2_comites', to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembro3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miembro3_comites', to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembro4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miembro4_comites', to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='comite',
            name='miembro5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miembro5_comites', to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='comite',
            name='solicitud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Curso'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Academico'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='solicitud',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='beca',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Estudiante'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='adscripcion',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Institucion'),
        ),
        migrations.AddField(
            model_name='adscripcion',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Perfil'),
        ),
        migrations.AddField(
            model_name='acuerdo',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='acta',
            name='sesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Sesion'),
        ),
        migrations.AddField(
            model_name='academico',
            name='campos_de_conocimiento',
            field=models.ManyToManyField(blank=True, to='posgradmin.CampoConocimiento'),
        ),
        migrations.AddField(
            model_name='academico',
            name='lineas_de_investigacion',
            field=models.ManyToManyField(blank=True, to='posgradmin.LineaInvestigacion'),
        ),
        migrations.AddField(
            model_name='academico',
            name='solicitud',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posgradmin.Solicitud'),
        ),
        migrations.AddField(
            model_name='academico',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]