from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from .models import Servico
from .forms import *
from cadastro.forms import FormEndereco

@login_required
def homeServico(request):
	servico = Servico.objects.filter(situacao=True).filter(status=False)
	template_name='servico/inicio_servico.html'
	return render(request, template_name, {'servicos_pendentes':servico},
		context_instance=RequestContext(request))


@permission_required('servico.add_servico', raise_exception=True)
@login_required
def adicionarServico(request):
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES)
		formEnd = FormEndereco(request.POST, request.FILES)
		if form.is_valid() and formEnd.is_valid():
			cad = form.save(commit=False)
			
			end = formEnd.save()
			
			cad.endereco = end
			cad.save()
			return render_to_response("salvo.html", {}, context_instance=RequestContext(request))
	else:
		form = FormServico()
		formEnd = FormEndereco()
	return render_to_response("servico/adicionar_servico.html", {'form':form, 
		'formEnd':formEnd}, context_instance=RequestContext(request))


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def listaServico(request):
	if request.user.Tipo.Tecnico and not request.user.is_staff:
		lista_servicos = Servico.objects.filter(
		funcionario=request.user).filter(situacao=True)
	else:
		lista_servicos = Servico.objects.filter(situacao=True)
	
	template_name='servico/lista_servico.html'
	return render(request, template_name, {'lista_servicos':lista_servicos},
		context_instance=RequestContext(request))


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def detalheServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	return render_to_response('servico/detalhe_servico.html', 
		{'servico':servico}, context_instance=RequestContext(request))


@permission_required('servico.change_servico', raise_exception=True)
@login_required
def editarServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	if request.method == "POST":
		form = FormServico(request.POST, request.FILES, instance=servico)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, context_instance=RequestContext(request))
	else:
		form = FormServico(instance=servico)
	return render_to_response("servico/adicionar_servico.html", {'form':form}, 
		context_instance=RequestContext(request))


@permission_required('servico.delete_servico', raise_exception=True)
@login_required
def removeServico(request, nr_item):
	servico = get_object_or_404(Servico, pk=nr_item)
	if request.method == "POST":
		servico.delete()
		return render_to_response("removido.html", {})
	return render_to_response("servico/remove_servico.html", {'servico':servico}, 
		context_instance=RequestContext(request))

@login_required
def homeEquipamento(request):
	total_equipamento = Equipamento.objects.all().count()
	equipamento_solicidato = Servico.objects.filter(equipamento=True).count()
	template_name='servico/inicio_equipamento.html'
	return render(request, template_name,
		{'total_equipamento':total_equipamento, 'equipamento_solicitado':equipamento_solicidato},
		context_instance=RequestContext(request))


@permission_required('servico.add_equipamento', raise_exception=True)
@login_required
def adicionarEquipamento(request):
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormEquipamento()
	return render_to_response("servico/adicionar_equipamento.html", {'form':form}, 
		context_instance=RequestContext(request))


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def listaEquipamento(request):
	lista_equipamento = Equipamento.objects.all()
	template_name='servico/lista_equipamento.html'
	return render(request, template_name, {'lista_equipamentos':lista_equipamento},
		context_instance=RequestContext(request))


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def detalheEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	return render_to_response('servico/datalhe_equipamento.html', {'equipamento':equipamento},
		context_instance=RequestContext(request))


@permission_required('servico.change_equipamento', raise_exception=True)
@login_required
def editarEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	if request.method == "POST":
		form = FormEquipamento(request.POST, request.FILES, instance=equipamento)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {},context_instance=RequestContext(request))
	else:
		form = FormEquipamento(instance=equipamento)
	
	return render_to_response("servico/adicionar_equipamento.html", {'form':form}, 
		context_instance=RequestContext(request))


@permission_required('servico.delete_equipamento', raise_exception=True)
@login_required
def removeEquipamento(request, nr_item):
	equipamento = get_object_or_404(Equipamento, pk=nr_item)
	if request.method == "POST":
		equipamento.delete()
		return render_to_response("removido.html", {})
	return render_to_response("servico/remove_equipamento.html", {'equipamento':equipamento}, 
		context_instance=RequestContext(request))