# Generated by Django 5.0.4 on 2024-04-25 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0002_alter_campus_options_alter_cursos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='cursoEstudante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piloto.cursos', verbose_name='Curso do Estudante'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='eImagem',
            field=models.ImageField(upload_to='', verbose_name='Foto do Estudante'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='modoDeEntrada',
            field=models.IntegerField(choices=[(1, 'Vestibular'), (2, 'SISU'), (3, 'PSEnem')], default='SISU', verbose_name='Modo de Entrada'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='situacaoEstudante',
            field=models.IntegerField(choices=[(1, 'Vinculado'), (2, 'Formado'), (3, 'Jubilado'), (4, 'Evadido')], default='VINCULADO', verbose_name='Situação do Estudante'),
        ),
    ]