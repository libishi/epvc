# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 23:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20170513_2252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bc',
        ),
        migrations.DeleteModel(
            name='faqs',
        ),
        migrations.DeleteModel(
            name='md',
        ),
        migrations.DeleteModel(
            name='mindec',
        ),
        migrations.DeleteModel(
            name='unsubscribe',
        ),
    ]
