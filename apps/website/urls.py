from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from apps.website import views 

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^sobre/$', views.Sobre.as_view(), name='sobre'),
    url(r'^participe/$', views.Participe.as_view(), name='participe'),
    url(r'^doar/$', views.Doacao.as_view(), name='doar'),
    url(r'^galeria/(?P<pk>\d+)/$', views.Galeria.as_view(), name='galeria'),
    url(r'^galeria/lista/$', views.ListaGaleria.as_view(), name='galeria-lista'),
    url(r'^noticia/(?P<pk>\d+)/$', views.Noticia.as_view(), name='noticia'),
    url(r'^noticia/lista/$', views.ListaNoticias.as_view(), name='noticia-lista'),
    url(r'^contato/$', views.Contato.as_view(), name='contato'),
]
