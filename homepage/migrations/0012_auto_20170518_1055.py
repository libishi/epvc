# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20170518_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvddl',
            name='month',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='pvnewsletters',
            name='month',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pvddl',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
