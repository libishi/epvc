# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-21 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_auto_20170521_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.CharField(max_length=200)),
                ('a', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='psur',
            old_name='rmp',
            new_name='paragraph',
        ),
    ]
