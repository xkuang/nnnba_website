# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nnnba', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playervalue',
            name='future_salary',
        ),
        migrations.RemoveField(
            model_name='playervalue',
            name='paid',
        ),
        migrations.AddField(
            model_name='player',
            name='future_salary',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='paid',
            field=models.FloatField(default=0),
        ),
    ]
