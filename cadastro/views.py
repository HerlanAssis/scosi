# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
#from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from .models import *
from servico.models import Servico

@login_required
def homeCadastro(request):
	usuarios = Usuario.objects.filter(
		is_superuser=False).filter(is_active=True)
	supervisores = Usuario.objects.filter(
		is_superuser=False).filter(is_active=True).filter(tipo=1)
	secretarios = Usuario.objects.filter(
		is_superuser=False).filter(is_active=True).filter(tipo=2)
	tecnicos = Usuario.objects.filter(
		is_superuser=False).filter(is_active=True).filter(tipo=3)

	context = {
		'usuarios':usuarios,
		'supervisores':supervisores,
		'secretarios':secretarios,
		'tecnicos':tecnicos,
	}

	template_name = 'cadastro/inicio_cadastro.html'

	return render(request, template_name, context)

@permission_required('cadastro.add_usuario', raise_exception=True)
@login_required
def adicionarCadastro(request):
	if request.method == "POST":
		form = FormUsuario(request.POST, request.FILES)
		formEnd = FormEndereco(request.POST, request.FILES)
		if form.is_valid() and formEnd.is_valid():
			cad = form.save(commit=False)

			end = formEnd.save()

			cad.endereco = end
			cad.save()
			return render(request, "salvo.html", {})
	else:
		form = FormUsuario()
		formEnd = FormEndereco()
	return render(request,"cadastro/adicionar_cadastro.html",
		{'form':form,'formEnd':formEnd})

@permission_required('cadastro.change_usuario', raise_exception=True)
@login_required
def listaCadastro(request):
	lista_cadastro = Usuario.objects.filter(is_superuser=False)
	template_name = 'cadastro/lista_cadastro.html'
	return render(request, template_name,
		{'lista_cadastros':lista_cadastro},)


@permission_required('cadastro.change_usuario', raise_exception=True)
@login_required
def detalheCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)
	template_name = 'cadastro/detalhe_cadastro.html'
	return render(request, template_name, {'cadastro':cadastro})


@permission_required('cadastro.change_usuario', raise_exception=True)
@login_required
def editarCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)

	if request.method == "POST":
		form = FormUsuario(request.POST, request.FILES, instance=cadastro)
		formEnd = FormEndereco(request.POST, request.FILES, instance=cadastro.endereco)
		if form.is_valid() and formEnd.is_valid():
			cad = form.save(commit=False)

			end = formEnd.save()

			cad.endereco = end
			cad.save()
			return render(request,"salvo.html", {})
	else:
		form = FormUsuario(instance=cadastro)
		formEnd = FormEndereco(instance=cadastro.endereco)
	return render(request,"cadastro/adicionar_cadastro.html",
		{'form':form,'formEnd':formEnd})


@permission_required('cadastro.delete_usuario', raise_exception=True)
@login_required
def removeCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)
	template_name = "cadastro/remove_cadastro.html"
	if request.method == "POST":
		try:
			cadastro.delete()
		except Exception, e:
			return render(request,"nao_permitido.html",{})
			
		return render(request,"removido.html", {})
	return render(request,template_name,{'cadastro':cadastro})


@login_required
def homeCliente(request):
	total_clientes = Cliente.objects.all().count()
	total_servicos = Servico.objects.all().count()
	total_servicos_concluidos = Servico.objects.filter(
		situacao=True).filter(status=True).count()
	total_servicos_cancelados = Servico.objects.filter(
		situacao=False).count()
	total_servicos_pendentes = Servico.objects.filter(
		situacao=True).filter(status=False).count()

	context = {
		'total_clientes' : total_clientes,
		'total_servicos' : total_servicos,
		'total_servicos_concluidos' : total_servicos_concluidos,
		'total_servicos_cancelados' : total_servicos_cancelados,
		'total_servicos_pendentes' : total_servicos_pendentes,
	}

	template_name = 'cadastro/inicio_cliente.html'
	return render(request, template_name, context)

@permission_required('cadastro.add_cliente', raise_exception=True)
@login_required
def adicionarCliente(request):
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES)
		formEnd = FormEndereco(request.POST, request.FILES)
		if form.is_valid() and formEnd.is_valid():
			cad = form.save(commit=False)

			end = formEnd.save()

			cad.endereco = end
			cad.save()
			return render(request,"salvo.html", {})
	else:
		form = FormCliente()
		formEnd = FormEndereco()
	return render(request,"cadastro/adicionar_cliente.html",
		{'form':form, 'formEnd':formEnd})


@permission_required('cadastro.change_cliente', raise_exception=True)
@login_required
def listaCliente(request):
	lista_clientes = Cliente.objects.all()
	template_name = 'cadastro/lista_cliente.html'
	return render(request, template_name, {'lista_clientes':lista_clientes},
		context_instance=RequestContext(request))


@permission_required('cadastro.change_cliente', raise_exception=True)
@login_required
def detalheCliente(request, nr_item):
	cliente = get_object_or_404(Cliente, pk=nr_item)
	template_name = 'cadastro/detalhe_cliente.html'
	return render(request,template_name, {'cliente':cliente})


@permission_required('cadastro.change_cliente', raise_exception=True)
@login_required
def editarCliente(request, nr_item):
	cliente = get_object_or_404(Cliente, pk=nr_item)
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES, instance=cliente)
		formEnd = FormEndereco(request.POST, request.FILES, instance=cliente.endereco)
		if form.is_valid() and formEnd.is_valid:
			cad = form.save(commit=False)

			end = formEnd.save()

			cad.endereco = end
			cad.save()
			return render(request,"salvo.html", {})
	else:
		form = FormCliente(instance=cliente)
		formEnd = FormEndereco(instance=cliente.endereco)
	return render(request, "cadastro/adicionar_cliente.html",
		{'form':form, 'formEnd':formEnd})


@permission_required('cadastro.delete_cliente', raise_exception=True)
@login_required
def removeCliente(request, nr_item):
	cliente = get_object_or_404(Cliente, pk=nr_item)
	if request.method == "POST":
		try:
			cliente.delete()
		except Exception, e:
			return render(request,"nao_permitido.html",{})
		
		return render(request,"removido.html", {})
	return render(request, "cadastro/remove_cliente.html",
		{'cliente':cliente})