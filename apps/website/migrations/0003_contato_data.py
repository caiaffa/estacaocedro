# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contato_is_visualizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='data',
            field=models.DateTimeField(auto_now=True, verbose_name='Data'),
        ),
    ]