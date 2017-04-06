from django import forms
from .models import Publicacao

class PublicacaoForm(forms.Form):
	titulo = forms.CharField(label='Título')
	imagem = forms.ImageField(label='Imagem')
	conteudo = forms.CharField(label='Conteúdo', widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(PublicacaoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['imagem'].widget.attrs['class'] = 'form-control'
		self.fields['conteudo'].widget.attrs['class'] = 'form-control summernote'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título da publicação'
		self.fields['imagem'].widget.attrs['placeholder'] = 'Imagem de capa da publicação'
		self.fields['conteudo'].widget.attrs['placeholder'] = 'Conteúdo da publicação'