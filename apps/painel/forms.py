from django import forms
from .models import Publicacao
from tinymce.widgets import TinyMCE

class PublicacaoForm(forms.Form):
	titulo = forms.CharField(label='Título')
	imagem = forms.CharField(label='Imagem')
	conteudo = forms.CharField(label='Conteúdo', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

	def __init__(self, *args, **kwargs):
		super(PublicacaoForm, self).__init__(*args, **kwargs)