from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Servico

@login_required
def homeServico(request):
	template_name='servico/inicio_servico.html'
	return render(request, template_name, {})

@login_required
def listaServico(request):
	lista_servicos = Servico.objects.all()
	template_name='servico/lista_servico.html'
	return render(request, template_name, {'lista_servicos':lista_servicos})

@login_required
def homeEquipamento(request):
	template_name='servico/inicio_equipamento.html'
	return render(request, template_name, {})

@login_required
def listaEquipamento(request):
	lista_equipamento = Equipamento.objects.all()
	template_name='servico/lista_equipamento.html'
	return render(request, template_name, {'lista_equipamento':lista_equipamento})