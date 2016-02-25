# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
	PermissionsMixin, Group)
#from django.contrib.auth.models import User
from djchoices import DjangoChoices, ChoiceItem
from localflavor.br.br_states import STATE_CHOICES


class Endereco(models.Model):
	TIPO_LOGRADOURO_CHOICES = (
		('rua', 'Rua'),
		('avenida', 'Avenida'),
		('travessa', 'Travessa'),
	)

	endereco_tipo_logradouro = models.CharField(max_length=10, choices=TIPO_LOGRADOURO_CHOICES, verbose_name='Tipo Logradouro')
	endereco_logradouro = models.CharField(max_length=80, verbose_name='Logradouro')
	endereco_numero = models.IntegerField(verbose_name='Número')
	endereco_complemento = models.CharField(max_length=45, blank=True, verbose_name='Complemento')
	endereco_bairro = models.CharField(max_length=80, verbose_name='Bairro')
	endereco_cidade = models.CharField(max_length=80, verbose_name='Cidade')
	endereco_estado = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='Estado')
	endereco_cep = models.CharField(max_length=9, blank=True, verbose_name='CEP')
	
	def __unicode__(self):
		return '%s %s, %s, %s, %s - %s' % (self.endereco_tipo_logradouro, self.endereco_logradouro, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado)
	class Meta:
		verbose_name = 'Endereço'
		verbose_name_plural = 'Endereços'
		ordering = ['endereco_tipo_logradouro']

class UsuarioManager(BaseUserManager):
	def create_user(self, cpf, nome, sobrenome, email,tipo, password=None):
		if not cpf:
			raise ValueError('Usuários devem possuir CPF')

		superuser = True if tipo == 99 else False
		user = self.model(cpf=cpf, nome=nome, sobrenome=sobrenome, email=email,tipo=tipo,
			is_superuser=superuser)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, cpf, nome, sobrenome, email, password):
		user = self.create_user(cpf, nome, sobrenome, email,
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
	endereco = models.ForeignKey(Endereco, null=True, verbose_name='endereço')
	is_active = models.BooleanField(default=True, verbose_name='ativo')
	tipo = models.PositiveIntegerField(choices=Tipo.choices, 
		default=Tipo.Tecnico, verbose_name='tipo de usuário')

	_default_manager = UsuarioManager()
	objects = _default_manager
	USERNAME_FIELD = 'cpf'
	REQUIRED_FIELDS = ['nome', 'sobrenome','email']

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

	'''@property
				def is_active(self):
					return self.ativo'''

	class Meta:
		verbose_name = 'usuário'
		verbose_name_plural = 'usuários'


@python_2_unicode_compatible
class Cliente(models.Model):
	SEXO_CHOICES = (
		('masculino', 'Masculino'),
		('feminino', 'Feminino'),
	)
	ESTADO_CIVIL_CHOICES = (
		('solteiro', 'Solteiro'),
		('casado', 'Casado'),
		('divorciado', 'Divorciado'),
		('viuvo', 'Viúvo'),
	)

	nome = models.CharField(max_length=30, verbose_name='nome')
	sobrenome = models.CharField(max_length=30, verbose_name='sobrenome')
	sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, verbose_name='sexo')
	estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES, verbose_name='estado civil')
	cpf = models.BigIntegerField(unique=True, verbose_name='CPF')
	codigo = models.CharField(max_length=20, unique=True, verbose_name='código')
	endereco = models.ForeignKey(Endereco, verbose_name='endereço', on_delete=models.PROTECT)

	def __str__(self):
		return "%s %s" % (self.nome, self.sobrenome)

	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'