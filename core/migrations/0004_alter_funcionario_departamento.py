# Generated by Django 3.2.4 on 2021-07-01 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(db_column='id_departamento', on_delete=django.db.models.deletion.DO_NOTHING, related_name='funcionarios', to='core.departamento'),
        ),
    ]
