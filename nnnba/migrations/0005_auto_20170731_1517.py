# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nnnba', '0004_auto_20170731_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coefficients',
            old_name='pts_2nd_chanCE',
            new_name='pts_2nd_chance',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='pts_2nd_chanCE',
            new_name='pts_2nd_chance',
        ),
    ]
