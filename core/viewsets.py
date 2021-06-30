from rest_framework import viewsets
from core import models, serializers


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Departamento.objects.all()
    serializer_class = serializers.DepartamentoSerializer

    def retrieve(self, request, *args, **kwargs):
        print('GET by ID')
        return super(DepartamentoViewSet, self).retrieve(request, *args, **kwargs)
