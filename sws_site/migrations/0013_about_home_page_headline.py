# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sws_site', '0012_auto_20161212_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='home_page_headline',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
