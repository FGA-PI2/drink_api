from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views

router = routers.SimpleRouter()

# router.register(r'users',UserViewSet)
router.register(r'bebida',BebidasViewSet)
router.register(r'racks',RackViewSet)
router.register(r'estoque',EstoqueViewSet)
router.register(r'compras',CompraViewSet)
router.register(r'quantidade-compra',QuantidadeCompraViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/',views.obtain_auth_token),
    url(r'users', UserViewList.as_view()),
]

urlpatterns += router.urls
