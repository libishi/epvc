# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-23 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_mymodel_subscribe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]