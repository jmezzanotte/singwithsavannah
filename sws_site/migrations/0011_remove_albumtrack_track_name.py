# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sws_site', '0010_albumtrack_track_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumtrack',
            name='track_name',
        ),
    ]