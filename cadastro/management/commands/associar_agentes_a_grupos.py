# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from siade.agentes.models import Agente
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for num, nome in Agente.Tipo.choices:
            grupo, c = Group.objects.get_or_create(name=nome)
            agentes_do_tipo = Agente.objects.filter(tipo=num)
            grupo.user_set.add(*agentes_do_tipo)
