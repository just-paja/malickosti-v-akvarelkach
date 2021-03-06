# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import visibility.models.visibility


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('event_type', models.PositiveIntegerField(choices=[(1, 'type-exposition'), (2, 'type-vernissage')], default=1, verbose_name='Type')),
                ('start', models.DateTimeField(verbose_name='field-start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='field-end')),
                ('all_day', models.BooleanField(default=False, help_text='field-all-day-help-text', verbose_name='field-all-day')),
                ('description', models.TextField(help_text='field-description-help-text')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(height_field='height', upload_to='var/texts', verbose_name='field-image', width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True, help_text='field-text-help-text', null=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='web.Event')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('address', models.CharField(help_text='field-address-help-text', max_length=255)),
                ('website', models.URLField(help_text='field-website-help-text')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Location'),
        ),
    ]
