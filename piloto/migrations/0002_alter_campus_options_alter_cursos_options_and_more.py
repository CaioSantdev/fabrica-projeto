# Generated by Django 5.0.4 on 2024-04-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name': 'Campus', 'verbose_name_plural': 'Campi'},
        ),
        migrations.AlterModelOptions(
            name='cursos',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='estudante',
            options={'verbose_name': 'Estudante', 'verbose_name_plural': 'Estudantes'},
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='dataAmoversarop',
        ),
        migrations.AddField(
            model_name='estudante',
            name='dataAniversario',
            field=models.DateField(null=True, verbose_name='Data de aniversário'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpfEstudante',
            field=models.CharField(max_length=14, unique=True, verbose_name='Cpf do Estudante'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='matriculaEstudante',
            field=models.CharField(max_length=9, unique=True, verbose_name='Matricula'),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='nomeEstudante',
            field=models.CharField(max_length=100, verbose_name='Nome do Estudante'),
        ),
    ]
