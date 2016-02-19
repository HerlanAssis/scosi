from cadastro.models import Usuario

Tecnico_permissions = (
	'servico.add_equipamento',
	'servico.change_equipamento',
	'servico.delete_equipamento',
	
	'servico.change_servico',
)

Secretaria_permissions = (
	'cadastro.add_uf',
	'cadastro.change_uf',
	'cadastro.delete_uf',

	'cadastro.add_municipio',
	'cadastro.change_municipio',
	'cadastro.delete_municipio',

	'cadastro.add_bairro',
	'cadastro.change_bairro',
	'cadastro.delete_bairro',

	'cadastro.add_logradouro',
	'cadastro.change_logradouro',
	'cadastro.delete_logradouro',

	'cadastro.add_usuario',
	'cadastro.change_usuario',

	'servico.add_equipamento',
	'servico.change_equipamento',
	'servico.delete_equipamento',

	'servico.add_servico',
	'servico.change_servico',
)

Supervisor_permissions = (
	'cadastro.add_uf',
	'cadastro.change_uf',
	'cadastro.delete_uf',

	'cadastro.add_municipio',
	'cadastro.change_municipio',
	'cadastro.delete_municipio',

	'cadastro.add_bairro',
	'cadastro.change_bairro',
	'cadastro.delete_bairro',

	'cadastro.add_logradouro',
	'cadastro.change_logradouro',
	'cadastro.delete_logradouro',

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
    Usuario.Tipo.Secretario: Secretaria_permissions,
    Usuario.Tipo.Tecnico: Tecnico_permissions,
}