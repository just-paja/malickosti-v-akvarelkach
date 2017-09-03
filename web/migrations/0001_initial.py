# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('description', models.TextField(help_text='Describe everything that user needs to know about this object.            You can format the text in Markdown')),
                ('price', models.PositiveIntegerField(default=0, help_text='This price will be added to Order in default currency')),
            ],
            options={
                'verbose_name': 'Delivery Method',
                'verbose_name_plural': 'Delivery Methods',
            },
        ),
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Aktuálně k prodeji'), (2, 'Zarezervováno'), (3, 'Prodáno')], default=1)),
                ('image', models.ImageField(height_field='image_height', upload_to='var/drawings', verbose_name='Image of drawing', width_field='image_width')),
                ('image_height', models.PositiveIntegerField(null=True)),
                ('image_width', models.PositiveIntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Drawing',
                'verbose_name_plural': 'Drawings',
            },
        ),
        migrations.CreateModel(
            name='DrawingPriceLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('price', models.PositiveIntegerField(help_text='This price will be added to Order in default currency')),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Drawing Price Level',
                'verbose_name_plural': 'Drawing Price Levels',
            },
        ),
        migrations.CreateModel(
            name='DrawingRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('kind', models.PositiveIntegerField(choices=[(1, 'Jiná velikost'), (2, 'Duplikát')])),
                ('child', models.ForeignKey(help_text='Child for this relationship. If you are not sure,          use object that is younger.', on_delete=django.db.models.deletion.CASCADE, related_name='drawings_parent', to='web.Drawing')),
                ('parent', models.ForeignKey(help_text='Parent for this relationship. If you are not sure,          use object that is older.', on_delete=django.db.models.deletion.CASCADE, related_name='drawings_child', to='web.Drawing')),
            ],
            options={
                'verbose_name': 'Drawing Relationship',
                'verbose_name_plural': 'Drawing Relationships',
            },
        ),
        migrations.CreateModel(
            name='DrawingSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('size_horizontal', models.PositiveIntegerField(help_text='How wide is the medium in milimeters')),
                ('size_vertical', models.PositiveIntegerField(help_text='How tall is the medium in milimeters')),
            ],
            options={
                'verbose_name': 'Drawing Size',
                'verbose_name_plural': 'Drawing Sizes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('event_type', models.PositiveIntegerField(choices=[(1, 'Výstava'), (2, 'Vernisáž')], default=1, verbose_name='Type')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('description', models.TextField(help_text='Describe everything that user needs to know about this object.            You can format the text in Markdown')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('address', models.CharField(help_text='Address in human readable format', max_length=255)),
                ('website', models.URLField(help_text='Website URL')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('buyer', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=63)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Nová'), (2, 'Potvrzená'), (3, 'Na cestě'), (4, 'Doručená'), (5, 'Zrušená')], default=1)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.DeliveryMethod')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDrawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='web.Drawing')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='web.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Very short description that helps to recognize the object', max_length=255)),
                ('description', models.TextField(help_text='Describe everything that user needs to know about this object.            You can format the text in Markdown')),
                ('price', models.PositiveIntegerField(default=0, help_text='This price will be added to Order in default currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Location'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='price_levels',
            field=models.ManyToManyField(to='web.DrawingPriceLevel'),
        ),
        migrations.AddField(
            model_name='drawing',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.DrawingSize'),
        ),
    ]
