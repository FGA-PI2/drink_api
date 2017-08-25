from django.conf.urls import url,include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()

router.register(r'users',UserViewSet)
router.register(r'bebida',BebidasViewSet)
router.register(r'racks',RackViewSet)
router.register(r'estoque',EstoqueViewSet)
router.register(r'compras',CompraViewSet)
router.register(r'quantidade-compra',QuantidadeCompraViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
