# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0004_auto_20170407_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacao',
            name='resumo',
            field=models.TextField(default=1, verbose_name='Breve Resumo'),
            preserve_default=False,
        ),
    ]
