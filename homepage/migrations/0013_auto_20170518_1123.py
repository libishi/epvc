# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20170518_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centernews',
            name='readmore',
            field=models.CharField(max_length=200, null=True),
        ),
    ]