from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from .forms import *
from .models import *

@login_required
def homeCadastro(request):
	template_name = 'cadastro/inicio_cadastro.html'
	return render(request, template_name, {}, context_instance=RequestContext(request))

@permission_required('cadastro.add_cadastro', raise_exception=True)
@login_required
def adicionarCadastro(request):
	if request.method == "POST":
		form = FormUsuario(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, context_instance=RequestContext(request))
	else:
		form = FormUsuario()
	return render_to_response("cadastro/adicionar_cadastro.html", {'form':form},
		context_instance=RequestContext(request))

@permission_required('cadastro.change_cadastro', raise_exception=True)
@login_required
def listaCadastro(request):
	lista_cadastro = Usuario.objects.filter(is_superuser=False)
	template_name = 'cadastro/lista_cadastro.html'
	return render(request, template_name, {'lista_cadastros':lista_cadastro},
		context_instance=RequestContext(request))


@permission_required('cadastro.change_cadastro', raise_exception=True)
@login_required
def detalheCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)
	return render_to_response('cadastro/detalhe_cadastro.html',
		{'cadastro':cadastro}, context_instance=RequestContext(request))


@permission_required('cadastro.change_cadastro', raise_exception=True)
@login_required
def editarCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)
	if request.method == "POST":
		form = FormUsuario(request.POST, request.FILES, instance=cadastro)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, context_instance=RequestContext(request))
	else:
		form = FormUsuario(instance=cadastro)
	
	return render_to_response("cadastro/adicionar_cadastro.html", {'form':form}, 
		context_instance=RequestContext(request))


@permission_required('cadastro.delete_cadastro', raise_exception=True)
@login_required
def removeCadastro(request, nr_item):
	cadastro = get_object_or_404(Usuario, pk=nr_item)
	if request.method == "POST":
		cadastro.delete()
		return render_to_response("removido.html", {},
			context_instance=RequestContext(request))
	return render_to_response("cadastro/remove_cadastro.html",
		{'cadastro':cadastro}, context_instance=RequestContext(request))


@login_required
def homeCliente(request):
	template_name = 'cadastro/inicio_cliente.html'
	return render(request, template_name, {}, context_instance=RequestContext(request))

@permission_required('cadastro.add_cliente', raise_exception=True)
@login_required
def adicionarCliente(request):
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCliente()
	return render_to_response("cadastro/adicionar_cliente.html", {'form':form}, 
		context_instance=RequestContext(request))


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
	return render_to_response('cadastro/detalhe_cliente.html',
		{'cliente':cliente}, context_instance=RequestContext(request))


@permission_required('cadastro.change_cliente', raise_exception=True)
@login_required
def editarCliente(request, nr_item):
	cliente = get_object_or_404(Usuario, pk=nr_item)
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES, instance=cliente)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, context_instance=RequestContext(request))
	else:
		form = FormUsuario(instance=cliente)
	
	return render_to_response("cadastro/adicionar_cliente.html", {'form':form}, 
		context_instance=RequestContext(request))


@permission_required('cadastro.delete_cliente', raise_exception=True)
@login_required
def removeCliente(request, nr_item):
	cliente = get_object_or_404(Cliente, pk=nr_item)
	if request.method == "POST":
		cliente.delete()
		return render_to_response("removido.html", {}, context_instance=RequestContext(request))
	return render_to_response("cadastro/remove_cliente.html", {'cliente':cliente}, 
		context_instance=RequestContext(request))