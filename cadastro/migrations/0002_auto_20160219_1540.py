# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.Logradouro', verbose_name='endere\xe7o'),
        ),
    ]
