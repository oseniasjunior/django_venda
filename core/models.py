from django.db import models


# Create your models here.
class Departamento(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', null=False, blank=False, max_length=100)
    ativo = models.BooleanField(db_column='cs_ativo', null=False, blank=False, default=True)

    class Meta:
        db_table = 'departamento'
        managed = True

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = ('M', 'Masculino')
        FEMININO = ('F', 'Feminino')

    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', null=False, blank=False, max_length=104)
    salario = models.DecimalField(db_column='nb_salario', null=False, blank=False, max_digits=10, decimal_places=2)
    sexo = models.CharField(db_column='cs_sexo', null=True, blank=True, max_length=1, choices=Sexo.choices)
    departamento = models.ForeignKey(
        to='Departamento',
        on_delete=models.DO_NOTHING,
        db_column='id_departamento',
        null=False,
        blank=False,
        related_name='funcionarios'
    )
    ativo = models.BooleanField(db_column='cs_ativo', null=False, blank=False, default=True)

    class Meta:
        db_table = 'funcionario'
        managed = True
