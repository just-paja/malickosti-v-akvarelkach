# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageIllustration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(height_field='image_height', upload_to='var/illustration', verbose_name='field-drawing-image', width_field='image_width')),
                ('position', models.PositiveIntegerField(choices=[(1, 'position_left'), (2, 'position_center'), (3, 'position_right')])),
                ('weight', models.PositiveIntegerField(default=0)),
                ('image_height', models.PositiveIntegerField(null=True)),
                ('image_width', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Homepage illustration',
                'verbose_name_plural': 'Homepage illustrations',
            },
        ),
    ]
