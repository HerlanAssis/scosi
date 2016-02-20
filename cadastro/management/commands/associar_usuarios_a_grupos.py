# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from cadastro.models import Usuario
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for num, nome in Usuario.Tipo.choices:
            grupo, c = Group.objects.get_or_create(name=nome)
            usuarios_do_tipo = Usuario.objects.filter(tipo=num)
            grupo.user_set.add(*usuarios_do_tipo)
