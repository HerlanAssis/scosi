from django.conf.urls import url
from views import *

from .views import *

app_name = 'cadastro'

urlpatterns = [
	url(r'^$', homeCadastro, name='homeCadastro'),
	url(r'^adicionar/$', adicionarCadastro, name='adicionarCadastro'),
	url(r'^listar/$', listaCadastro, name='listarCadastro'),
	
	url(r'^cliente/$', homeCliente, name='homeCliente'),
	url(r'^cliente/adicionar/$', adicionarCliente, name='adicionarCliente'),
	url(r'^cliente/listar/$', listaCliente, name='listarCliente'),
]