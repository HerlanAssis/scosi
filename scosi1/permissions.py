from cadastro.models import Usuario, UF, Municipio, Bairro, Logradouro
from servico.models import Servicos, Equipamento

Tecnico_permissions = (
	'usuario.usuario',
	
	'servico.change_servico',

	'equipamento.add_equipamento',
	'equipamento.change_equipamento',
	'equipamento.delete_equipamento',

)

Secretaria_permissions = (
	'usuario.change_usuario',

	'uf.add_uf',
	'uf.change_uf',
	'uf.delete_uf',

	'municipio.add_municipio',
	'municipio.change_municipio',
	'municipio.delete_municipio',

	'bairro.add_bairro',
	'bairro.change_bairro',
	'bairro.delete_bairro',

	'logradouro.add_logradouro',
	'logradouro.change_logradouro',
	'logradouro.delete_logradouro',

	'servico.add_servico',
	'servico.change_servico',
	'servico.delete_servico',

	'equipamento.add_equipamento',
	'equipamento.change_equipamento',
	'equipamento.delete_equipamento',
)

Supervisor_permissions = (
	'cliente.add_cliente',
	'cliente.change_cliente',
	'cliente.delete_cliente',

	'usuario.add_usuario',
	'usuario.change_usuario',
	'usuario.delete_usuario',

	'uf.add_uf',
	'uf.change_uf',
	'uf.delete_uf',

	'municipio.add_municipio',
	'municipio.change_municipio',
	'municipio.delete_municipio',

	'bairro.add_bairro',
	'bairro.change_bairro',
	'bairro.delete_bairro',

	'logradouro.add_logradouro',
	'logradouro.change_logradouro',
	'logradouro.delete_logradouro',

	'servico.add_servico',
	'servico.change_servico',
	'servico.delete_servico',

	'equipamento.add_equipamento',
	'equipamento.change_equipamento',
	'equipamento.delete_equipamento',
)

Administrador_permissions = tuple(Supervisor_permissions + (
))

GROUP_PERMISSIONS = {
    Usuario.tipo.Supervisor: Administrador_permissions,
    Usuario.tipo.Tecnico: Tecnico_permissions,
    Usuario.tipo.Secretaria: Secretaria_permissions,
}