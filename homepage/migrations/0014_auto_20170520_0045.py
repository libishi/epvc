# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-20 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_auto_20170518_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centernews2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('readmore', models.CharField(max_length=200, null=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Centernews3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('readmore', models.CharField(max_length=200, null=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Centernewsmain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('readmore', models.CharField(max_length=200, null=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Centernews',
            new_name='Centernews1',
        ),
    ]
