# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from apps.painel.models import Publicacao
from apps.website.models import Contato
from .forms import PublicacaoForm


class Home(View):
    def get(self, request):
        return render (request, 'core/index.html')


class PublicacaoRegister(View):
    def get(self, request):
        form = PublicacaoForm()
        context = {'form':form}
        return render (request, 'publicacao/register.html', context)

    def post(self, request):
        form = PublicacaoForm(request.POST, request.FILES)
        context = {'form':form}
        if form.is_valid():
            publicacao = Publicacao()
            publicacao.usuario = request.user
            publicacao.titulo = request.POST.get('titulo')
            publicacao.imagem = request.FILES.get('imagem')
            publicacao.conteudo = request.POST.get('conteudo')
            publicacao.save()
            return redirect(reverse_lazy("publicacao-list"))
        else:
            return render (request, 'publicacao/register.html', context)

class PublicacaoList(View):
    def get(self, request):
        obj_list = Publicacao.objects.all()

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            publicacoes = paginator.page(page)
        except PageNotAnInteger:
            publicacoes = paginator.page(1)
        except EmptyPage:
            publicacoes = paginator.page(paginator.num_pages)
        context = {'publicacoes': publicacoes}
        return render(request, 'publicacao/list.html', context)


class ContatoList(View):
    def get(self, request):
        obj_list = Contato.objects.all()

        paginator = Paginator(obj_list, 25)
        page = request.GET.get('page')
        try:
            contatos = paginator.page(page)
        except PageNotAnInteger:
            contatos = paginator.page(1)
        except EmptyPage:
            contatos = paginator.page(paginator.num_pages)
        context = {'contatos': contatos}
        return render(request, 'contato/list.html', context)