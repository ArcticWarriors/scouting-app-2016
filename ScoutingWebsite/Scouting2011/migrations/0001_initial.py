# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compitition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchNumber', models.IntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Compitition')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchNumber', models.IntegerField()),
                ('hasOfficialData', models.BooleanField(default=False)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Compitition')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scored_uber_tube', models.BooleanField()),
                ('low_tubes_hung', models.IntegerField()),
                ('mid_tubes_hung', models.IntegerField()),
                ('high_tubes_hung', models.IntegerField()),
                ('tubes_dropped', models.IntegerField()),
                ('tubes_received', models.IntegerField()),
                ('minibot_finish', models.IntegerField()),
                ('deployed_minibot', models.BooleanField()),
                ('penelties', models.IntegerField()),
                ('was_offensive', models.BooleanField()),
                ('was_scouted', models.BooleanField()),
                ('broke_badly', models.BooleanField()),
                ('comments', models.CharField(max_length=1000)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Compitition')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamNumber', models.IntegerField()),
                ('homepage', models.CharField(default=b'', max_length=2000)),
                ('rookie_year', models.CharField(max_length=4)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('team_nickname', models.CharField(max_length=100)),
                ('robot_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeamComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCompetesIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Compitition')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=1000)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Team')),
            ],
        ),
        migrations.AddField(
            model_name='scoreresult',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scouting2011.Team'),
        ),
    ]
