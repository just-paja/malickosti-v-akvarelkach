# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='eventphoto',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventPhoto',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
