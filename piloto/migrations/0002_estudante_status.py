# Generated by Django 5.0.4 on 2024-05-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piloto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='status',
            field=models.IntegerField(choices=[(1, 'Vinculado'), (2, 'Formado'), (3, 'Jubilado'), (4, 'Evadido'), (5, 'INATIVO')], default=1, verbose_name='Status'),
        ),
    ]
