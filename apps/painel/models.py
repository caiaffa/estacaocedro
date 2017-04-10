from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicacao(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	resumo = models.TextField('Breve Resumo')
	imagem = models.ImageField('Imagem')
	conteudo = models.TextField('Conteúdo')
	data = models.DateTimeField('Data de Publicação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)

class Projeto(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	descricao = models.TextField('Descrição')
	data = models.DateTimeField('Data de Publicação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)


class Album(models.Model):
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	data_album = models.DateField('Data do Evento')
	data = models.DateTimeField('Data de Criação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)


class Imagem(models.Model):
	album = models.ForeignKey(Album)
	imagem = models.ImageField('Foto')


