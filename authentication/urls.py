from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views

router = routers.SimpleRouter()

# router.register(r'users',UserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/',views.obtain_auth_token),
    url(r'user', UserViewList.as_view()),
]

urlpatterns += router.urls
