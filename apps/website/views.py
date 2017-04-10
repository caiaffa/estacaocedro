# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

from .forms import ContatoForm
from apps.painel.models import Publicacao, Projeto

class Home(View):
    def get(self, request):
    	publicacoes = Publicacao.objects.all().order_by('-data')[:3]
    	projetos = Projeto.objects.all().order_by('-data')[:6]
    	context = {'publicacoes':publicacoes, 'projetos':projetos}
    	return render (request, 'index.html', context)

class Noticias(View):
	def get(self, request, pk):
		publicacao = Publicacao.objects.get(pk=pk)
		context = {'publicacao':publicacao}
		return render(request, 'noticia.html', context)

class Contato(View):
	def get(self, request):
		form = ContatoForm
		context = {'form':form, 'message':False}
		return render (request, 'contato.html', context)

	def post(self, request, *args, **kwargs):
		form = ContatoForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
		form = ContatoForm()
		context = {'form':form, 'message':True}
		return render (request, 'contato.html', context)