# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, unique=True, verbose_name='Título')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('conteudo', tinymce.models.HTMLField(verbose_name='HTML')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de Publicação')),
            ],
        ),
    ]
