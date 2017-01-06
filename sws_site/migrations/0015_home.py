# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sws_site', '0014_auto_20161231_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_headline', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Page',
                'get_latest_by': 'timestamp',
            },
        ),
    ]
