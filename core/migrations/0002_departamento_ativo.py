# Generated by Django 3.2.4 on 2021-07-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='ativo',
            field=models.BooleanField(db_column='cs_ativo', default=True),
        ),
    ]
