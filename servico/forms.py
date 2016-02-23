from django import forms

from cadastro.models import Usuario
from .models import *

class FormEquipamento(forms.ModelForm):
	class Meta:
		model = Equipamento

		fields = ['codigo', 'nome', 'descricao']

class FormServico(forms.ModelForm):
	class Meta:
		model = Servico

		fields = ['tipo', 'codigo', 'data_de_inicio', 'data_de_fim', 'descricao', 
		'valor', 'status', 'situacao', 'funcionario', 'cliente', 'equipamento', 'logradouro']
		
		widgets = {
			'data_de_inicio': forms.SelectDateWidget,
			'data_de_fim': forms.SelectDateWidget,
		}

	def __init__(self, *args, **kwargs):
		super(FormServico, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['funcionario'].queryset = Usuario.objects.filter(
				is_superuser=False)