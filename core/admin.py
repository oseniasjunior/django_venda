from django.contrib import admin
from core import models


# Register your models here.

@admin.register(models.Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'salario']
    search_fields = ['nome']

