from django import forms
from .models import *


class FormUF(forms.ModelForm):
	class Meta:
		model = UF

		fields = ['nome', 'sigla']

class FormMunicipio(forms.ModelForm):
	class Meta:
		model = Municipio

		fields = ['nome', 'uf']

class FormBairro(forms.ModelForm):
	class Meta:
		model = Bairro

		fields = ['nome', 'municipio']

class FormLogradouro(forms.ModelForm):
	class Meta:
		model = Logradouro

		fields = ['nome', 'bairro']

class FormUsuario(forms.ModelForm):
	class Meta:
		model = Usuario

		fields = ['cpf', 'tipo', 'telefone', 'nascimento', 'endereco', 'codigo', 'ativo']

class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente

		fields = ['nome', 'sobrenome', 'cpf', 'endereco']