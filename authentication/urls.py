from django.conf.urls import url,include
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()

router.register(r'users',UserViewList)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/',views.obtain_auth_token),
]

urlpatterns += format_suffix_patterns(urlpatterns)
