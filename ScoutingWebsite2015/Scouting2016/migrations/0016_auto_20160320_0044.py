# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scouting2016', '0015_auto_20160319_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='bookmark',
        ),
        migrations.AlterField(
            model_name='team',
            name='teamAlliances',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
