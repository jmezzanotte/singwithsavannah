# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-04 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170104_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
