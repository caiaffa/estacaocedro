from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.painel import views 

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),

	# URLS PUBLICAÇÃO
	url(r'^publicacao/$', login_required(views.PublicacaoList.as_view()), name='publicacao-listar'),
    url(r'^publicacao/cadastrar/$', login_required(views.PublicacaoRegister.as_view()), name='publicacao-cadastrar'),
    
    # URLS CONTATO
    url(r'^contato/$', views.ContatoList.as_view(), name='contato-listar'),
]