# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from .models import Servico
from .forms import *
from cadastro.forms import FormEndereco

@login_required
def homeServico(request):
	if request.user.tipo == Usuario.Tipo.Tecnico:
		servico = Servico.objects.filter(
		funcionario=request.user).filter(situacao=True).filter(status=False)
	else:
		servico = Servico.objects.filter(situacao=True).filter(status=False)

	template_name='servico/inicio_servico.html'
	context = {'servicos_pendentes':servico}

	return render(request, template_name, context)


@permission_required('servico.add_servico', raise_exception=True)
@login_required
def adicionarServico(request):
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES)
		formEndereco = FormEndereco(request.POST, request.FILES)
		if form.is_valid() and formEndereco.is_valid():
			cad = form.save(commit=False)
			end = formEndereco.save()

			cad.endereco = end

			cad.save()
			form.save_m2m()
			return render(request, "salvo.html", {})
	else:
		form = FormServico()
		formEndereco = FormEndereco()
	return render(request,"servico/adicionar_servico.html",
		{'form':form, 'formEnd':formEndereco})


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def listaServico(request):
	if request.user.tipo == Usuario.Tipo.Tecnico:
		lista_servicos = Servico.objects.filter(
		funcionario=request.user).filter(situacao=True)
	else:
		lista_servicos = Servico.objects.filter(situacao=True)

	template_name='servico/lista_servico.html'
	context = {'lista_servicos':lista_servicos}
	return render(request, template_name, context)


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def detalheServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	template_name = 'servico/detalhe_servico.html'
	context = {'servico': servico}
	return render(request, template_name, context)


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def editarServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES, instance=servico)
		formEnd = FormEndereco(request.POST, request.FILES, instance=servico.endereco)
		if form.is_valid() and formEnd.is_valid():
			cad = form.save(commit=False)

			end = formEnd.save()

			cad.endereco = end
			cad.save()
			form.save_m2m()
			return render(request,"salvo.html", {})
	else:
		form = FormServico(instance=servico)
		formEnd = FormEndereco(instance=servico.endereco)
	return render(request,"servico/adicionar_servico.html",
		{'form':form,'formEnd':formEnd})


@permission_required('servico.delete_servico', raise_exception=True)
@login_required
def removeServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	context = {'servico':servico}
	if request.method == "POST":
		try:
			servico.delete()
		except Exception, e:
			return render(request,"nao_permitido.html",{})
			
		return render(request,"removido.html", {})
	return render(request, "servico/remove_servico.html", context)



@login_required
def homeEquipamento(request):
	total_equipamento = Equipamento.objects.all().count()
	equipamento_solicidato = Servico.objects.filter(equipamento=True).count()
	template_name='servico/inicio_equipamento.html'

	context = {
		'total_equipamento':total_equipamento,
		'equipamento_solicitado':equipamento_solicidato
	}

	return render(request, template_name,context)

@permission_required('servico.add_equipamento', raise_exception=True)
@login_required
def adicionarEquipamento(request):
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request,"salvo.html", {})
	else:
		form = FormEquipamento()
	return render(request, "servico/adicionar_equipamento.html",
		{'form':form})


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def listaEquipamento(request):
	lista_equipamento = Equipamento.objects.all()
	template_name='servico/lista_equipamento.html'
	context = {'lista_equipamentos':lista_equipamento}
	return render(request, template_name, context)


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def detalheEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	template_name = 'servico/datalhe_equipamento.html'
	context = {'equipamento':equipamento}
	return render(request, template_name, context)


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def editarEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES, instance=equipamento)
		if form.is_valid():
			form.save()
			return render(request, "salvo.html", {})
	else:
		form = FormEquipamento(instance=equipamento)

	return render(request, "servico/adicionar_equipamento.html",
		{'form':form})


@permission_required('servico.delete_equipamento', raise_exception=True)
@login_required
def removeEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	context = {'equipamento':equipamento}
	if request.method == "POST":
		try:
			equipamento.delete()
		except Exception, e:
			return render(request,"nao_permitido.html",{})
		
		return render(request,"removido.html", {})
	return render(request, "servico/remove_equipamento.html", context)