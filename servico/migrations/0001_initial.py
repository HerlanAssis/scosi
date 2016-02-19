# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 18:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, max_length=300, verbose_name='descricao')),
            ],
            options={
                'ordering': ('nome',),
                'verbose_name': 'Equipamento',
                'verbose_name_plural': 'Equipamentos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=300, verbose_name='descricao')),
                ('data_de_cadastro', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='data de cadastro')),
                ('data_de_inicio', models.DateTimeField(default=datetime.datetime.now, verbose_name='data de in\xedcio do servi\xe7o')),
                ('data_de_fim', models.DateTimeField(verbose_name='data de fim do servi\xe7o')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='valor do servi\xe7o')),
                ('tipo', models.CharField(choices=[('INS', 'Instala\xe7\xe3o'), ('MAN', 'Manuten\xe7\xe3o'), ('REM', 'Remo\xe7\xe3o'), ('SUP', 'Suporte')], default='INS', max_length=30, verbose_name='tipo de servi\xe7o')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('situacao', models.BooleanField(default=True, verbose_name='situa\xe7\xe3o')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Cliente', verbose_name='cliente')),
                ('equipamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servico.Equipamento', verbose_name='equipamento')),
                ('funcionario', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='funcion\xe1rio')),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Logradouro', verbose_name='endere\xe7o')),
            ],
            options={
                'ordering': ('data_de_cadastro',),
                'verbose_name': 'servi\xe7o',
                'verbose_name_plural': 'servi\xe7os',
            },
        ),
    ]
