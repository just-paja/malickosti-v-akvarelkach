# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20171007_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpayment',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'In progress'), (2, 'Paid'), (3, 'Cancelled')], default=2),
        ),
    ]
