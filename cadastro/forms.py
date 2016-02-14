from django import forms
from .models import *

class FormUsuario(forms.ModelForm):
	class Meta:
		model = Usuario

class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente

class FormUF(forms.ModelForm):
	class Meta:
		model = UF

class FormMunicipio(forms.ModelForm):
	class Meta:
		model = Municipio

class FormBairro(forms.ModelForm):
	class Meta:
		model = Bairro

class FormLogradouro(forms.ModelForm):
	class Meta:
		model = Logradouro