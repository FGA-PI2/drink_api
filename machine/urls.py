from django.conf.urls import url,include
from rest_framework import routers
from views import *


router = routers.SimpleRouter()

router.register(r'users',UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns += router.urls
