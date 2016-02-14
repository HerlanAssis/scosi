from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def homeCadastro(request):
	template_name = 'cadastro/inicio_cadastro.html'
	return render(request, template_name, {'hello':'hello'})

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
def listaCliente(request):
	lista_cadastro = Cliente.objects.all()
	template_name = 'cadastro/lista_cliente.html'
	return render(request, template_name, {'lista_cadastros':lista_cadastro})