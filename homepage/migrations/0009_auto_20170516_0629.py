# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20170514_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ddl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('ddl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='psur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmp', models.TextField()),
                ('guidelines', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pvnewsletters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('newsletter', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmp', models.TextField()),
                ('guidelines', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='pv',
            old_name='address',
            new_name='pv',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='mail1',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='mail2',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='mail3',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='tele1',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='tele2',
        ),
        migrations.RemoveField(
            model_name='pv',
            name='tele3',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='contact_details',
            field=models.CharField(max_length=200),
        ),
    ]