from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.website import views 

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^contato/$', views.Contato.as_view(), name='contato'),
]
