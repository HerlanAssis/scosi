# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from .. import create_or_update_groups


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        create_or_update_groups()
        print "Grupos atualizados"
