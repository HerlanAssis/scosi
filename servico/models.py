#! -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#<-- My imports
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
from cadastro.models import Usuario, Cliente, Logradouro
#My imports -->

@python_2_unicode_compatible
class Equipamento(models.Model):

	nome = models.CharField(max_length=30, verbose_name='nome')
	descricao = models.CharField(max_length=100, blank=True, verbose_name='descricao')

	def __str__(self):
		return "%s - %s" % (self.nome, self.descricao)

	class Meta:
		verbose_name = 'Equipamento'
		verbose_name_plural = 'Equipamentos'
		ordering = ("nome",)


@python_2_unicode_compatible
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
	data_de_cadastro = models.DateTimeField(default=datetime.now, editable=False, verbose_name='data de cadastro')
	data_de_inicio = models.DateTimeField(default=datetime.now, verbose_name='data de início do serviço')
	data_de_fim = models.DateTimeField(verbose_name='data de fim do serviço')
	valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='valor do serviço', default=0)
	tipo = models.CharField(blank=False, max_length=30, choices=TIPO_DE_SERVICO, verbose_name='tipo de serviço', default=INSTALACAO)
	
	#dados do serviço
	status = models.BooleanField(verbose_name='status', default=False)
	situacao = models.BooleanField(verbose_name='situação', default=True)

	#relações
	funcionario = models.ManyToManyField(Usuario, verbose_name='funcionário')
	cliente = models.ForeignKey(Cliente, verbose_name='cliente')
	equipamento = models.ForeignKey(Equipamento, blank=True, null=True, verbose_name='equipamento')
	logradouro = models.ForeignKey(Logradouro, verbose_name='endereço')

	def __str__(self):
		return "%i: %s-%s" % (self.id, self.data_de_inicio, self.data_de_fim)

	class Meta:
		verbose_name = 'serviço'
		verbose_name_plural = 'serviços'
		ordering = ("data_de_cadastro",)