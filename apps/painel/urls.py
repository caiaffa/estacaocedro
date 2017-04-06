from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.painel import views 

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),

	# URLS PUBLICAÇÃO
	url(r'^publicacao/$', login_required(views.PublicacaoList.as_view()), name='publicacao-listar'),
    url(r'^publicacao/cadastrar/$', login_required(views.PublicacaoRegister.as_view()), name='publicacao-cadastrar'),
    url(r'^publicacao/editar/(?P<pk>\d+)/$', views.PublicacaoEdit.as_view(), name='publicacao-editar'),
    url(r'^publicacao/deletar/(?P<pk>\d+)/$', views.PublicacaoDelete.as_view(), name='publicacao-deletar'),

    # URLS CONTATO
    url(r'^mensagem/$', views.ContatoList.as_view(), name='contato-listar'),
    url(r'^mensagem/visualizar/(?P<pk>\d+)/$', views.ContatoDetail.as_view(), name='contato-detalhes'),
    url(r'^mensagem/deletar/(?P<pk>\d+)/$', views.ContatoDelete.as_view(), name='contato-deletar'),
]