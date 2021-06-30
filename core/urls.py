from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('departamentos', viewsets.DepartamentoViewSet)

urlpatterns = router.urls
