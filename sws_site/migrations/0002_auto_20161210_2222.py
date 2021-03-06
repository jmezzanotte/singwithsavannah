# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sws_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_icon',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='service',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]
