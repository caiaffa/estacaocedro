from django import forms
from .models import Publicacao

class PublicacaoForm(forms.Form):
	titulo = forms.CharField(label='Título')
	imagem = forms.CharField(label='Imagem')
	conteudo = forms.CharField(label='Conteúdo', widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(PublicacaoForm, self).__init__(*args, **kwargs)