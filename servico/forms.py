from django import forms

from .models import *

class FormEquipamento(forms.ModelForm):
	class Meta:
		model = Equipamento

class FormServico(forms.ModelForm):
	class Meta:
		model = Servico
