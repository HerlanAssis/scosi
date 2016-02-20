import re
from django import forms
from django.contrib.auth import (authenticate, get_user_model,
	password_validation,)
from django.utils.encoding import smart_text
from localflavor.br.forms import BRPhoneNumberField, BRCPFField
from input_mask.contrib.localflavor.br.widgets import (BRPhoneNumberInput,
	BRCPFInput)
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import *

class ReadOnlyPasswordHashWidget(forms.Widget):
	def render(self, name, value, attrs):
		encoded = value
		final_attrs = self.build_attrs(attrs)

		if not encoded or encoded.startswith(UNUSABLE_PASSWORD_PREFIX):
			summary = mark_safe("<strong>%s</strong>" % ugettext("No password set."))
		else:
			try:
				hasher = identify_hasher(encoded)
			except ValueError:
				summary = mark_safe("<strong>%s</strong>" % ugettext("Invalid password format or unknown hashing algorithm."))
			else:
				summary = format_html_join('',
					"<strong>{}</strong>: {} ",
					((ugettext(key), value)
						for key, value in hasher.safe_summary(encoded).items()))

		return format_html("<div{}>{}</div>", flatatt(final_attrs), summary)

class CPFInput(BRCPFInput):
	def render(self, name, value, attrs=None):
		value = str(value).zfill(11)
		return super(CPFInput, self).render(name, value, attrs)

	def value_from_datadict(self, data, files, name):
		value = data.get('cpf')
		if not value.isdigit():
			value = re.sub("[-\. ]", "", value)
		return value

class FormUF(forms.ModelForm):
	class Meta:
		model = UF

		fields = ['nome', 'sigla']

class FormMunicipio(forms.ModelForm):
	class Meta:
		model = Municipio

		fields = ['nome', 'uf']

class FormBairro(forms.ModelForm):
	class Meta:
		model = Bairro

		fields = ['nome', 'municipio']

class FormLogradouro(forms.ModelForm):
	class Meta:
		model = Logradouro

		fields = ['nome', 'bairro']

class FormUsuario(forms.ModelForm):
	error_messages = {
		'password_mismatch': _("The two password fields didn't match."),
	}

	cpf = BRCPFField(widget=CPFInput, label='CPF')
	telefone = BRPhoneNumberField(widget=BRPhoneNumberInput, required=False)
	password1 = forms.CharField(label=_("Password"), 
		widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"),
		widget=forms.PasswordInput,
	help_text=_("Enter the same password as before, for verification."))

	def __init__(self, *args, **kwargs):
		super(FormUsuario, self).__init__(*args, **kwargs)
		self.fields['cpf'].widget.attrs.update({'autofocus': ''})

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		self.instance.cpf = self.cleaned_data.get('cpf')
		password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
		return password2

	def save(self, commit=True):
		user = super(FormUsuario, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

	def clean_telefone(self):
		value = self.cleaned_data['telefone']
		value = re.sub('-', '', smart_text(value))
		if value == '':
			return None
		else:
			return int(value)
	
	class Meta:
		model = Usuario

		fields = ['cpf', 'tipo', 'nome', 'sobrenome', 'email',
		'telefone', 'nascimento', 'endereco', 'codigo',]

class FormCliente(forms.ModelForm):
	cpf = BRCPFField(widget=CPFInput, label='CPF')
	telefone = BRPhoneNumberField(widget=BRPhoneNumberInput, required=False)
	
	def clean_telefone(self):
		value = self.cleaned_data['telefone']
		value = re.sub('-', '', smart_text(value))
		if value == '':
			return None
		else:
			return int(value)
	class Meta:
		model = Cliente
		
		fields = ['nome', 'sobrenome', 'codigo', 'cpf', 'endereco']