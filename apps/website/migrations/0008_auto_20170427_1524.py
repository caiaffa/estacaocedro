# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20170417_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='celular',
            field=models.CharField(blank=True, max_length=21, null=True, verbose_name='Telefone Celular'),
        ),
    ]
