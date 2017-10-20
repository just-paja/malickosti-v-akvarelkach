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
        ('drawings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('description', models.TextField(help_text='field-description-help-text')),
                ('price', models.PositiveIntegerField(default=0, help_text='field-method-price-help-text', verbose_name='field-price')),
                ('weight', models.PositiveIntegerField(default=0, help_text='field-weight-help-text', verbose_name='field-weight')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
            ],
            options={
                'verbose_name': 'Delivery Method',
                'verbose_name_plural': 'Delivery Methods',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('buyer', models.CharField(help_text='field-buyer-help-text', max_length=255, verbose_name='field-buyer')),
                ('email', models.EmailField(max_length=254, verbose_name='field-email')),
                ('phone', models.CharField(max_length=63, verbose_name='field-phone')),
                ('address', models.CharField(help_text='field-address-help-text', max_length=63, verbose_name='field-address')),
                ('price', models.PositiveIntegerField(verbose_name='field-price')),
                ('paid', models.BooleanField(default=False, verbose_name='field-paid')),
                ('over_paid', models.BooleanField(default=False, verbose_name='field-over-paid')),
                ('symvar', models.CharField(blank=True, max_length=63, unique=True, verbose_name='field-symvar')),
                ('status', models.PositiveIntegerField(choices=[(1, 'status-new'), (2, 'status-confirmed'), (3, 'status-on-route'), (4, 'status-delivered'), (5, 'status-canceled')], default=1, verbose_name='field-status')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.DeliveryMethod', verbose_name='field-delivery-method')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDrawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('drawing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='drawings.Drawing')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='eshop.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ident', models.CharField(blank=True, help_text='field-payment-ident-help-text', max_length=255, null=True, verbose_name='field-payment-ident')),
                ('symvar', models.CharField(blank=True, max_length=255, null=True, verbose_name='field-symvar')),
                ('symcon', models.CharField(blank=True, max_length=255, null=True, verbose_name='field-symcon')),
                ('symspc', models.CharField(blank=True, max_length=255, null=True, verbose_name='field-symspc')),
                ('amount', models.CharField(max_length=255, verbose_name='field-amount')),
                ('sender', models.CharField(blank=True, default='unknown', help_text='field-payment-sender-help-text', max_length=255, verbose_name='field-payment-sender')),
                ('bank', models.CharField(blank=True, default='unknown', max_length=255, verbose_name='Bank')),
                ('currency', models.CharField(blank=True, default='unknown', max_length=255, verbose_name='field-currency')),
                ('received_at', models.DateTimeField(blank=True, help_text='field-received-at-help-text', null=True, verbose_name='field-received-at')),
                ('message', models.TextField(blank=True, max_length=255, null=True, verbose_name='field-message')),
                ('status', models.PositiveIntegerField(choices=[(1, 'status-in-progress'), (2, 'status-paid'), (3, 'status-canceled')], default=2, verbose_name='field-status')),
                ('user_identification', models.CharField(blank=True, help_text='field-user-identification-help-text', max_length=255, null=True, verbose_name='field-user-identification')),
                ('order', models.ForeignKey(blank=True, help_text='Which order is this payment related to?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='eshop.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order Payment',
                'verbose_name_plural': 'Order Payments',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('description', models.TextField(help_text='field-description-help-text')),
                ('needs_account_info', models.BooleanField(default=False, help_text='field-payment-method-need-account-info-help-text')),
                ('price', models.PositiveIntegerField(default=0, help_text='field-method-price-help-text', verbose_name='field-price')),
                ('weight', models.PositiveIntegerField(default=0, help_text='field-weight-help-text', verbose_name='field-weight')),
                ('visibility', visibility.models.visibility.VisibilityField(choices=[(1, 'visibility-public'), (2, 'visibility-private')], default=1, verbose_name='field-visibility')),
            ],
            options={
                'verbose_name': 'Payment Method',
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='PriceLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='field-name-help-text', max_length=255, verbose_name='field-name')),
                ('price', models.PositiveIntegerField(help_text='field-method-price-help-text', verbose_name='field-price')),
                ('valid_from', models.DateField(blank=True, null=True, verbose_name='field-valid-from')),
                ('valid_until', models.DateField(blank=True, null=True, verbose_name='field-valid-until')),
                ('drawings', models.ManyToManyField(related_name='price_levels', to='eshop.PriceLevel', verbose_name='field-price-levels')),
            ],
            options={
                'verbose_name': 'Price Level',
                'verbose_name_plural': 'Price Levels',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.PaymentMethod', verbose_name='field-payment-method'),
        ),
        migrations.AddField(
            model_name='deliverymethod',
            name='payment_methods',
            field=models.ManyToManyField(to='eshop.PaymentMethod'),
        ),
    ]
