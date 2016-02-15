from django.conf.urls import url
from views import *

from .views import *

app_name = 'servico'

urlpatterns = [
	url(r'^$', homeServico, name='homeServico'),
	url(r'^adicionar/$', adicionarServico, name='adicionarServico'),
	url(r'^listar/$', listaServico, name='listarServico'),
	url(r'^detalhe/(?P<nr_item>\d+)/$', detalheServico, name='detalheServico'),
	url(r'^editar/(?P<nr_item>\d+)/$', editarServico, name='editarServico'),
	
	url(r'^equipamento/$', homeEquipamento, name='homeEquipamento'),
	url(r'^equipamento/adicionar/$', adicionarEquipamento, name='adicionarEquipamento'),
	url(r'^equipamento/listar/$', listaEquipamento, name='listarEquipamento'),
	url(r'^equipamento/detalhe/(?P<nr_item>\d+)/$', detalheEquipamento, name='detalheEquipamento'),
	url(r'^equipamento/editar/(?P<nr_item>\d+)/$', editarEquipamento, name='editarEquipamento'),
]