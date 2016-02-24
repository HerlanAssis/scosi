from django.shortcuts import render_to_response
from django.template import RequestContext
from cadastro.models import Usuario, Cliente
from servico.models import Servico

def home(request):
	todos_usuarios = Usuario.objects.all().order_by('-dataCadastro').filter(
		is_active=True).filter(is_superuser=False)[:5]
	todos_clientes = Cliente.objects.all().order_by('-pk')[:5]
	todos_servicos = Servico.objects.all().order_by(
		'-data_de_cadastro').filter(situacao=True).filter(status=False)[:5]

	context = {
		'todos_usuarios': todos_usuarios,
		'todos_clientes': todos_clientes,
		'todos_servicos': todos_servicos,
	}

	template_name='home.html'
	return render_to_response(template_name, context,
		context_instance=RequestContext(request))