# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.template import RequestContext
from django.http import (JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseRedirect)
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PublicacaoForm
import json


class PublicacaoRegister(View):
    def get(self, request):
    	form = PublicacaoForm()
    	return render (request, 'publicacao_register.html', {'form':form})
