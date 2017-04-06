from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicacao(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(User)
	titulo = models.CharField('Título', max_length=50, unique=True)
	imagem = models.ImageField('Imagem')
	conteudo = models.CharField('Conteúdo', max_length=5000)
	data = models.DateTimeField('Data de Publicação', default=timezone.now)

	def __str__(self):
	    return str(self.titulo)