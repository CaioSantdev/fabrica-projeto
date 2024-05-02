# Generated by Django 5.0.4 on 2024-05-02 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Campus')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do curso')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piloto.campus', verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, verbose_name='Nome do Estudante')),
                ('cpfEstudante', models.CharField(max_length=14, unique=True, verbose_name='CPF do Estudante')),
                ('matricula', models.CharField(max_length=9, unique=True, verbose_name='Matricula')),
                ('dataAniversario', models.DateField(null=True, verbose_name='Data de aniversário')),
                ('eImagem', models.ImageField(upload_to='piloto/img/%Y/%m/%d', verbose_name='Foto do Estudante')),
                ('situacao', models.IntegerField(choices=[(1, 'Vinculado'), (2, 'Formado'), (3, 'Jubilado'), (4, 'Evadido')], default='VINCULADO', verbose_name='Situação do Estudante')),
                ('modoDeEntrada', models.IntegerField(choices=[(1, 'Vestibular'), (2, 'SISU'), (3, 'PSEnem')], default='SISU', verbose_name='Modo de Entrada')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piloto.curso', verbose_name='Curso do Estudante')),
            ],
            options={
                'verbose_name': 'Estudante',
                'verbose_name_plural': 'Estudantes',
            },
        ),
    ]
