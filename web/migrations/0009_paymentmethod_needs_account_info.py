# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_eventphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='needs_account_info',
            field=models.BooleanField(default=False),
        ),
    ]
