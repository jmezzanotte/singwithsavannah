# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-07 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogmain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmain',
            options={'get_latest_by': 'timestamp', 'verbose_name': 'Blog Main', 'verbose_name_plural': 'Blog Main'},
        ),
    ]