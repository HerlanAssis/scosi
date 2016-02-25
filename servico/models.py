# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#<-- My imports
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from cadastro.models import Usuario, Cliente, Endereco
#My imports -->

@python_2_unicode_compatible
class Equipamento(models.Model):

	nome = models.CharField(max_length=30, verbose_name='nome')
	descricao = models.TextField(max_length=300, blank=True, verbose_name='descricao')
	codigo = models.CharField(max_length=20, unique=True, verbose_name=u'código')

	def __str__(self):
		return "%s - %s" % (self.nome, self.descricao)

	class Meta:
		verbose_name = 'Equipamento'
		verbose_name_plural = 'Equipamentos'
		ordering = ("nome",)


#@python_2_unicode_compatible
class Servico(models.Model):

	INSTALACAO = 'INS'
	MANUTENCAO = 'MAN'
	REMOCAO = 'REM'
	SUPORTE = 'SUP'

	TIPO_DE_SERVICO = (
		(INSTALACAO, 'Instalação'),
		(MANUTENCAO, 'Manutenção'),
		(REMOCAO, 'Remoção'),
		(SUPORTE, 'Suporte'),
	)

	descricao = models.TextField(max_length=300, verbose_name='descricao')
	data_de_cadastro = models.DateTimeField(default=timezone.now, editable=False, verbose_name='data de cadastro')
	data_de_inicio = models.DateField(default=timezone.now, verbose_name='data de início do serviço')
	data_de_fim = models.DateField(verbose_name='data de fim do serviço')
	valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='valor do serviço', default=0)
	tipo = models.CharField(blank=False, max_length=30, choices=TIPO_DE_SERVICO,
		verbose_name='tipo de serviço', default=INSTALACAO)
	codigo = models.CharField(max_length=20, unique=True, verbose_name=u'código')
	
	#dados do serviço
	status = models.BooleanField(verbose_name='concluido', default=False)
	situacao = models.BooleanField(verbose_name='ativo', default=True)

	#relações
	funcionario = models.ManyToManyField(Usuario, verbose_name='funcionário')
	cliente = models.ForeignKey(Cliente, verbose_name='cliente',
		on_delete=models.PROTECT)
	equipamento = models.ForeignKey(Equipamento, blank=True, null=True,
		verbose_name='equipamento', on_delete=models.PROTECT)
	endereco = models.ForeignKey(Endereco, verbose_name='endereço',
		on_delete=models.PROTECT)

	def __str__(self):
		return "Código: %s" % (self.codigo)

	def funcionarios(self):
		return Usuario.objects.filter(servico__id=self.id)

	def andamento(self):
		if self.situacao and self.status:
			return "Concluido!"
		elif self.situacao and not self.status:
			return "Pendente!"
		else:
			return "Cancelado!"

	class Meta:
		verbose_name = 'serviço'
		verbose_name_plural = 'serviços'
		ordering = ('data_de_cadastro',)