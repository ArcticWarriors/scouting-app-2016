# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scouting2016', '0012_team_bookmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='bookmark',
            field=models.CharField(max_length=1000),
        ),
    ]