from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from apps.painel import views 

urlpatterns = [
	url(r'^$', login_required(views.Home.as_view()), name='home'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    
	# URLS PUBLICAÇÃO
	url(r'^publicacao/$', login_required(views.PublicacaoList.as_view()), name='publicacao-listar'),
    url(r'^publicacao/cadastrar/$', login_required(views.PublicacaoRegister.as_view()), name='publicacao-cadastrar'),
    url(r'^publicacao/editar/(?P<pk>\d+)/$', views.PublicacaoEdit.as_view(), name='publicacao-editar'),
    url(r'^publicacao/deletar/(?P<pk>\d+)/$', views.PublicacaoDelete.as_view(), name='publicacao-deletar'),

    # URLS CONTATO
    url(r'^mensagem/$', views.ContatoList.as_view(), name='contato-listar'),
    url(r'^mensagem/visualizar/(?P<pk>\d+)/$', views.ContatoDetail.as_view(), name='contato-detalhes'),
    url(r'^mensagem/deletar/(?P<pk>\d+)/$', views.ContatoDelete.as_view(), name='contato-deletar'),

    # URLS PROJETO
    url(r'^projeto/$', login_required(views.ProjetoList.as_view()), name='projeto-listar'),
    url(r'^projeto/cadastrar/$', login_required(views.ProjetoRegister.as_view()), name='projeto-cadastrar'),
    url(r'^projeto/editar/(?P<pk>\d+)/$', views.ProjetoEdit.as_view(), name='projeto-editar'),
    url(r'^projeto/deletar/(?P<pk>\d+)/$', views.ProjetoDelete.as_view(), name='projeto-deletar'),
]