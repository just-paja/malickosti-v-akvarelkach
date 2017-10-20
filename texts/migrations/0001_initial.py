# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 12:14
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
            name='AboutText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('text', models.TextField(help_text='field-text-help-text')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
                ('weight', models.PositiveIntegerField(default=0, help_text='field-weight-help-text', verbose_name='field-weight')),
            ],
            options={
                'verbose_name': 'About text',
                'verbose_name_plural': 'About texts',
            },
        ),
        migrations.CreateModel(
            name='AboutTextPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(height_field='height', upload_to='var/texts', verbose_name='field-image', width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True, help_text='field-text-help-text', null=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='texts.AboutText')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConditionsText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('text', models.TextField(help_text='field-text-help-text')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
                ('weight', models.PositiveIntegerField(default=0, help_text='field-weight-help-text', verbose_name='field-weight')),
            ],
            options={
                'verbose_name': 'Trade Conditions',
                'verbose_name_plural': 'Trade Conditions',
            },
        ),
        migrations.CreateModel(
            name='ConditionsTextPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(height_field='height', upload_to='var/texts', verbose_name='field-image', width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True, help_text='field-text-help-text', null=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='texts.ConditionsText')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('text', models.TextField(help_text='field-text-help-text')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
                ('weight', models.PositiveIntegerField(default=0, help_text='field-weight-help-text', verbose_name='field-weight')),
            ],
            options={
                'verbose_name': 'Contact text',
                'verbose_name_plural': 'Contact texts',
            },
        ),
        migrations.CreateModel(
            name='ContactTextPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(height_field='height', upload_to='var/texts', verbose_name='field-image', width_field='width')),
                ('height', models.PositiveIntegerField(null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True, help_text='field-text-help-text', null=True)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='texts.ContactText')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
                'abstract': False,
            },
        ),
    ]
