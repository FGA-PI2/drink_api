from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views

router = routers.SimpleRouter()

# router.register(r'users',UserViewSet)
router.register(r'bebida',BebidasViewSet)
router.register(r'compra',CompraViewSet)
router.register(r'pedido',PedidoViewSet)
router.register(r'code',QrCodeViewSet)
router.register(r'drink',DrinkViewSet)
router.register(r'cardapio',CardapioViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
