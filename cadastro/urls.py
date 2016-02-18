from django.conf.urls import url
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
]