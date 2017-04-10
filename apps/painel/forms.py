from django import forms
from django.contrib.auth import authenticate
from .models import Publicacao, Projeto

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


class LoginForm(forms.Form):
	usuario = forms.CharField(label='Usuário',required=True,max_length=50)
	password = forms.CharField(label='Senha',required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		if cleaned_data.get("usuario") and cleaned_data.get("password"):
			user = authenticate(username=cleaned_data.get("usuario"), password=cleaned_data.get("password"))
			if not user:
				self.add_error('password', 'Usuário e/ou senha inválido(s)')


class ProjetoForm(forms.ModelForm):
	class Meta:
		model = Projeto
		fields = ['titulo', 'descricao']

	def __init__(self, *args, **kwargs):
		super(ProjetoForm, self).__init__(*args, **kwargs)
		self.fields['titulo'].widget.attrs['class'] = 'form-control'
		self.fields['descricao'].widget.attrs['class'] = 'form-control'

		self.fields['titulo'].widget.attrs['placeholder'] = 'Título do projeto'
		self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição do projeto'

		self.fields['titulo'].widget.attrs['data-validation'] = '[NOTEMPTY]'
		self.fields['descricao'].widget.attrs['data-validation'] = '[NOTEMPTY]'