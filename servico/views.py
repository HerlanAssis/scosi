from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Servico
from .forms import *

@login_required
def homeServico(request):
	template_name='servico/inicio_servico.html'
	return render(request, template_name, {})

@login_required
def adicionarServico(request):
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormServico()
	return render_to_response("servico/adicionar_servico.html", {'form':form}, 
		context_instance=RequestContext(request))

@login_required
def listaServico(request):
	lista_servicos = Servico.objects.all()
	template_name='servico/lista_servico.html'
	return render(request, template_name, {'lista_servicos':lista_servicos})

@login_required
def detalheServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	return render_to_response('cadastro/detalhe_servico.html', {'servico':servico})

@login_required
def editarServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES, instance=servico)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormServico(instance=servico)
	return render_to_response("servico/adicionar_servico.html", {'form':form}, 
		context_instance=RequestContext(request))

@login_required
def homeEquipamento(request):
	template_name='servico/inicio_equipamento.html'
	return render(request, template_name, {})

@login_required
def adicionarEquipamento(request):
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormEquipamento()
	return render_to_response("servico/adicionar_equipamento.html", {'form':form}, 
		context_instance=RequestContext(request))

@login_required
def listaEquipamento(request):
	lista_equipamento = Equipamento.objects.all()
	template_name='servico/lista_equipamento.html'
	return render(request, template_name, {'lista_equipamentos':lista_equipamento})

@login_required
def detalheEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	return render_to_response('servico/datalhe_equipamento.html', {'equipamento':equipamento})

@login_required
def editarEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES, instance=equipamento)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormEquipamento(instance=equipamento)
	
	return render_to_response("servico/adicionar_equipamento.html", {'form':form}, 
		context_instance=RequestContext(request))