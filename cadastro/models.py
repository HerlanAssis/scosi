#! -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
	PermissionsMixin, Group)
from django.contrib.auth.models import User
from djchoices import DjangoChoices, ChoiceItem

@python_2_unicode_compatible
class UF(models.Model):
	'''
	Uma Unidade Federativa
	'''
	nome = models.CharField(max_length=100, verbose_name='nome')
	sigla = models.CharField(max_length=3, verbose_name='sigla')

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'estado'
		verbose_name_plural = 'estados'
		ordering = ('nome',)


@python_2_unicode_compatible
class Municipio(models.Model):
	'''
	Município de uma UF
	'''
	nome = models.CharField(max_length=100, verbose_name='nome')
	uf = models.ForeignKey(UF, verbose_name='UF', on_delete=models.PROTECT)

	def __str__(self):
		return "%s/%s" % (self.nome, self.uf.sigla)

	class Meta:
		verbose_name = 'município'
		verbose_name_plural = 'municípios'
		ordering = ('nome',)


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


@python_2_unicode_compatible
class Logradouro(models.Model):

	nome = models.CharField(max_length=100, verbose_name='logradouro')
	bairro = models.ForeignKey(Bairro, blank=False, on_delete=models.PROTECT)

	def __str__(self):
		return "%s, %s" % (self.nome, self.bairro)

	class Meta:
		verbose_name = 'logradouro'
		verbose_name_plural = 'logradouros'
		ordering = ('bairro', 'nome',)


class UsuarioManager(BaseUserManager):
	def create_user(self, cpf, nome, sobrenome, tipo, password=None):
		if not cpf:
			raise ValueError('Usuários devem possuir CPF')

		superuser = True if tipo == 99 else False
		user = self.model(cpf=cpf, nome=nome, sobrenome=sobrenome, tipo=tipo,
			is_superuser=superuser)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, cpf, nome, sobrenome, password):
		user = self.create_user(cpf, nome, sobrenome,
			99,password=password)
		return user


@python_2_unicode_compatible
class Usuario(AbstractBaseUser, PermissionsMixin):   

	class Tipo(DjangoChoices):
		''' Possiveis tipos para um usuário '''
		Supervisor = ChoiceItem(1, label='Supervisor')
		Secretario = ChoiceItem(2, label='Secretário')
		Tecnico = ChoiceItem(3, label='Técnico')
	
	cpf = models.BigIntegerField(unique=True, verbose_name='CPF')
	nome = models.CharField(max_length=30, verbose_name='nome')
	sobrenome = models.CharField(max_length=30, verbose_name='sobrenome')
	codigo = models.CharField(max_length=20, unique=True, verbose_name='código',
		help_text='Ex.: FUN123')
	email = models.EmailField(blank=True, verbose_name='e-mail')
	telefone = models.BigIntegerField(blank=True, null=True,
		verbose_name='telefone')
	nascimento = models.DateField(blank=True, null=True,
		verbose_name='data de nasc.')
	dataCadastro = models.DateTimeField(verbose_name='data de cadastro',
		default=timezone.now)
	endereco = models.ForeignKey(Logradouro, null=True, verbose_name='endereço')
	codigo = models.CharField(max_length=20, unique=True,
		verbose_name='código')
	ativo = models.BooleanField(default=True, verbose_name='ativo')
	tipo = models.PositiveIntegerField(choices=Tipo.choices, 
		default=Tipo.Tecnico, verbose_name='tipo de usuário')

	_default_manager = UsuarioManager()
	objects = _default_manager
	USERNAME_FIELD = 'cpf'
	REQUIRED_FIELDS = ['nome', 'sobrenome',]

	def __str__(self):
		return "%s" % self.nome

	
	def save(self, *args, **kwargs):
		super(Usuario, self).save(*args, **kwargs)
		
		try:
			group = Group.objects.get(name=self.get_tipo_display())
			self.groups.clear()
			self.groups.add(group)
		except:
			pass

	@property
	def first_name(self):
		return self.nome

	@property
	def last_name(self):
		return self.sobrenome

	def get_short_name(self):
		return self.nome

	def get_full_name(self):
		return '%s %s' % (self.nome, self.sobrenome)

	@property
	def is_staff(self):
		return self.is_superuser or self.tipo == 99

	@property
	def is_active(self):
		return self.ativo

	class Meta:
		verbose_name = 'usuário'
		verbose_name_plural = 'usuários'


@python_2_unicode_compatible
class Cliente(models.Model):
	nome = models.CharField(max_length=30, verbose_name='nome')
	sobrenome = models.CharField(max_length=30, verbose_name='sobrenome')
	cpf = models.BigIntegerField(unique=True, verbose_name='CPF')
	codigo = models.CharField(max_length=20, unique=True, verbose_name='código')
	endereco = models.ForeignKey(Logradouro, verbose_name='endereço')

	def __str__(self):
		return "%s" % self.nome

	class Meta:
		verbose_name = 'cliente'
		verbose_name_plural = 'clientes'