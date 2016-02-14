#! -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User

GLOBALPERMISSIONS = (
	("pode_ver", "Pode ver"),
	("pode_adicionar", "Pode adicionar"),
	("pode_editar", "Pode editar"),
	("pode_excluir", "Pode excluir"),
)

@python_2_unicode_compatible
class UF(models.Model):
	'''
	Uma Unidade Federativa
	'''
	nome = models.CharField(max_length=100)
	sigla = models.CharField(max_length=3)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'estado'
		verbose_name_plural = 'estados'
		ordering = ('nome',)

		permissions = tuple(GLOBALPERMISSIONS + (
		))


@python_2_unicode_compatible
class Municipio(models.Model):
	'''
	Município de uma UF
	'''
	nome = models.CharField(max_length=100)
	uf = models.ForeignKey(UF, verbose_name='UF')

	def __str__(self):
		return "%s/%s" % (self.nome, self.uf.sigla)

	class Meta:
		verbose_name = 'município'
		verbose_name_plural = 'municípios'
		ordering = ('nome',)

		permissions = tuple(GLOBALPERMISSIONS + (
		))


@python_2_unicode_compatible
class Bairro(models.Model):
	'''
	Bairro de um município
	'''
	nome = models.CharField(max_length=100, verbose_name='nome')
	municipio = models.ForeignKey(Municipio, related_name='bairros', 
		verbose_name='município', on_delete=models.PROTECT)

	def __str__(self):
		return "%s - %s" % (self.nome, self.municipio)

	class Meta:
		verbose_name = 'bairro'
		verbose_name_plural = 'bairros'
		ordering = ('nome',)

		permissions = tuple(GLOBALPERMISSIONS + (
		))


@python_2_unicode_compatible
class Logradouro(models.Model):

	nome = models.CharField(max_length=100, verbose_name='logradouro')
	bairro = models.ForeignKey(Bairro, blank=False)

	def __str__(self):
		return "%s, %s" % (self.nome, self.bairro)

	class Meta:
		verbose_name = 'logradouro'
		verbose_name_plural = 'logradouros'
		ordering = ('bairro', 'nome',)

		permissions = tuple(GLOBALPERMISSIONS + (
		))

@python_2_unicode_compatible
class Usuario(models.Model):    
	usuario = models.ForeignKey(User, verbose_name='usuário')

	SUPERVISOR = 1
	SECRETARIO = 2
	TECNICO = 3

	TIPO_DE_USUARIO = (
		(SUPERVISOR, 'Supervisor'),
		(SECRETARIO, 'Secretario'),
		(TECNICO, 'Técnico'),
	)
	
	tipo = models.PositiveIntegerField(choices=TIPO_DE_USUARIO, blank=False, default=SUPERVISOR, verbose_name='tipo de usuário')
	cpf = models.BigIntegerField(unique=True, verbose_name='CPF')
	endereco = models.ForeignKey(Logradouro, verbose_name='endereço')

	def __str__(self):
		return "%s" % self.usuario.username
	
	class Meta:
		verbose_name = 'usuário'
		verbose_name_plural = 'usuários'

		permissions = tuple(GLOBALPERMISSIONS + (
		))

@python_2_unicode_compatible
class Cliente(models.Model):
	nome = models.CharField(max_length=30, verbose_name='nome')
	sobrenome = models.CharField(max_length=30, verbose_name='sobrenome')
	cpf = models.BigIntegerField(unique=True, verbose_name='CPF')
	endereco = models.ForeignKey(Logradouro, verbose_name='endereço')

	def __str__(self):
		return "%s" % self.nome

	class Meta:
		verbose_name = 'cliente'
		verbose_name_plural = 'clientes'