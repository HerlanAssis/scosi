# -*- coding: utf-8 -*-
from cadastro.models import Usuario

Tecnico_permissions = (
	'cadastro.add_endereco',
	'cadastro.change_endereco',
	'cadastro.delete_endereco',
	
	'servico.add_equipamento',
	'servico.change_equipamento',
	'servico.delete_equipamento',
	
	'servico.change_servico',

)

Secretario_permissions = (

	'cadastro.add_endereco',
	'cadastro.change_endereco',
	'cadastro.delete_endereco',

	'cadastro.add_cliente',
	'cadastro.change_cliente',

	'servico.add_equipamento',
	'servico.change_equipamento',
	'servico.delete_equipamento',

	'servico.add_servico',
	'servico.change_servico',
)

Supervisor_permissions = (
	
	'cadastro.add_endereco',
	'cadastro.change_endereco',
	'cadastro.delete_endereco',

	'cadastro.add_usuario',
	'cadastro.change_usuario',
	'cadastro.delete_usuario',

	'cadastro.add_cliente',
	'cadastro.change_cliente',
	'cadastro.delete_cliente',

	'servico.add_equipamento',
	'servico.change_equipamento',
	'servico.delete_equipamento',

	'servico.add_servico',
	'servico.change_servico',
	'servico.delete_servico',
)

Administrador_permissions = tuple(Supervisor_permissions + (
))

GROUP_PERMISSIONS = {
    Usuario.Tipo.Supervisor: Administrador_permissions,
    Usuario.Tipo.Secretario: Secretario_permissions,
    Usuario.Tipo.Tecnico: Tecnico_permissions,
}