from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.painel import views 

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),
    url(r'^publicacao/cadastrar/$', views.PublicacaoRegister.as_view(), name='publicacao-cadastrar'),

    url(r'^contato/$', views.ContatoList.as_view(), name='contato-listar'),
]