from django import forms

from .models import *

class FormEquipamento(forms.ModelForm):
	class Meta:
		model = Equipamento

		fields = ['nome', 'descricao']

class FormServico(forms.ModelForm):
	class Meta:
		model = Servico

		fields = ['tipo', 'data_de_inicio', 'data_de_fim', 'descricao', 
		'valor', 'status', 'situacao', 'funcionario', 'cliente', 'equipamento', 'logradouro']