# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-14 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sws_site', '0004_auto_20170406_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.TextField()),
                ('written_by', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Testimonials',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]