from django import forms
from .models import Publicacao

class PublicacaoForm(forms.ModelForm):
	class Meta:
		model = Publicacao
		fields = ['titulo', 'resumo', 'imagem', 'conteudo']

	def __init__(self, *args, **kwargs):
		super(PublicacaoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['resumo'].widget.attrs['class'] = 'form-control'
		self.fields['imagem'].widget.attrs['class'] = 'form-control'
		self.fields['conteudo'].widget.attrs['class'] = 'form-control summernote'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título da publicação'
		self.fields['resumo'].widget.attrs['placeholder'] = 'Breve resumo da publicação'
		self.fields['imagem'].widget.attrs['placeholder'] = 'Imagem de capa da publicação'
		self.fields['conteudo'].widget.attrs['placeholder'] = 'Conteúdo da publicação'

		self.fields['titulo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['resumo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['conteudo'].widget.attrs['data-validation'] = '[NOTEMPTY]'