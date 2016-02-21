from django.conf.urls import url
from django.contrib.auth.views import (password_change, password_change_done, 
	password_reset, password_reset_done, password_reset_confirm, password_reset_complete)
from .views import *


app_name = 'cadastro'

urlpatterns = [
	url(r'^$', homeCadastro, name='homeCadastro'),
	url(r'^adicionar/$', adicionarCadastro, name='adicionarCadastro'),
	url(r'^listar/$', listaCadastro, name='listarCadastro'),
	url(r'^detalhe/(?P<nr_item>\d+)/$', detalheCadastro, name='detalheCadastro'),
	url(r'^editar/(?P<nr_item>\d+)/$', editarCadastro, name='editarCadastro'),
	url(r'^remove/(?P<nr_item>\d+)/$', removeCadastro, name='removeCadastro'),
	
	url(r'^cliente/$', homeCliente, name='homeCliente'),
	url(r'^cliente/adicionar/$', adicionarCliente, name='adicionarCliente'),
	url(r'^cliente/listar/$', listaCliente, name='listarCliente'),
	url(r'^cliente/detalhe/(?P<nr_item>\d+)/$', detalheCliente, name='detalheCliente'),
	url(r'^cliente/editar/(?P<nr_item>\d+)/$', editarCliente, name='editarCliente'),
	url(r'^cliente/remove/(?P<nr_item>\d+)/$', removeCliente, name='removeCliente'),

	url(r'^alterar-senha/$', password_change,
		{'template_name': 'password_change_form.html', 'post_change_redirect':'cadastro:senha-alterada'},
		name='alterar-senha'),
	url(r'^senha-alterada/$', password_change_done,	
		{'template_name': 'password_change_done.html'},
		name='senha-alterada'),
	url(r'^recuperar-senha/$', password_reset, 
		{'post_reset_redirect' : 'cadastro:senha-recuperada'}, name='recuperar-senha'),
	url(r'^senha-recuperada/$', password_reset_done, name='senha-recuperada'),
	url(r'^recuperar-senha-email/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
		{'post_reset_redirect' : 'cadastro:senha-email-recuperada'}, name='recuperar-senha-email'),
	url(r'^senha-email-recuperada/$', password_reset_complete, name='senha-email-recuperada'),
]