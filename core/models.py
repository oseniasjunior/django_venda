from django.db import models


# Create your models here.
class Departamento(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(db_column='tx_nome', null=False, max_length=100)

    class Meta:
        db_table = 'departamento'
        managed = True

    def __str__(self):
        return self.nome
