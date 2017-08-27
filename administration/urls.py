from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views

router = routers.SimpleRouter()

# router.register(r'users',UserViewSet)
router.register(r'bebida',BebidasViewSet)
router.register(r'rack',RackViewSet)
router.register(r'estoque',EstoqueViewSet)
router.register(r'compra',CompraViewSet)
router.register(r'pedido',PedidoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
