# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-21 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvnewsletters',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
