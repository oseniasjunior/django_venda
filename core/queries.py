from core import models
from django.db.models import F, Value, ExpressionWrapper, FloatField


def salario_10_pc():
    slario_10_pc = ExpressionWrapper(F('salario') + Value(10), output_field=FloatField())
    queryset = models.Funcionario.objects.annotate(salario_10_pc=slario_10_pc)
    return queryset


