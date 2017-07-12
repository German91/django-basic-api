from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]