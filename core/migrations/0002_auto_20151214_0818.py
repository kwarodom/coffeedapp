# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(blank=True, null=True),
        ),
    ]