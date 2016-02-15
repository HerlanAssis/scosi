from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import *
from .models import *

@login_required
def homeCadastro(request):
	template_name = 'cadastro/inicio_cadastro.html'
	return render(request, template_name, {'hello':'hello'})

@login_required
def adicionarCadastro(request):
	if request.method == "POST":
		form = FormUsuario(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormUsuario()
	return render_to_response("cadastro/adicionar_cadastro.html", {'form':form}, 
		context_instance=RequestContext(request))

@login_required
def listaCadastro(request):
	lista_cadastro = Usuario.objects.all()
	template_name = 'cadastro/lista_cadastro.html'
	return render(request, template_name, {'lista_cadastros':lista_cadastro})


@login_required
def homeCliente(request):
	template_name = 'cadastro/inicio_cliente.html'
	return render(request, template_name, {'hello':'hello'})

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

@login_required
def listaCliente(request):
	lista_cadastro = Cliente.objects.all()
	template_name = 'cadastro/lista_cliente.html'
	return render(request, template_name, {'lista_cadastros':lista_cadastro})