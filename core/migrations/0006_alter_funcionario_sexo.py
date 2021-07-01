# Generated by Django 3.2.4 on 2021-07-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_funcionario_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='cs_sexo', max_length=1, null=True),
        ),
    ]