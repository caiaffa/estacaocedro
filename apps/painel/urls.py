from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.painel import views 

urlpatterns = [
    url(r'^publicacao/cadastrar/$', views.PublicacaoRegister.as_view(), name='publicacao_register'),
]