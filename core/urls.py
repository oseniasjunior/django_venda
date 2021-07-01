from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('departamentos', viewsets.DepartamentoViewSet)
router.register('funcionarios', viewsets.FuncionarioViewSet)

urlpatterns = router.urls
