from rest_framework import viewsets
from core import models, serializers


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Departamento.objects.all()
    serializer_class = serializers.DepartamentoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = models.Funcionario.objects.all()
    serializer_class = serializers.FuncionarioSerializer
