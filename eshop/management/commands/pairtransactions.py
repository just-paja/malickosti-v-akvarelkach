#!/usr/bin/env python
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from fiobank import FioBank

from ...models import Order, OrderPayment


class Command(BaseCommand):
    help = 'Parses FIO bank statements'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days-back',
            default=7,
            type=int,
            nargs="?",
            help='Days back, for which will be the statement fetched',
        )

    def handle(self, *args, **kwargs):
        client = FioBank(token=settings.FIO_TOKEN)
        payments = client.period(
            datetime.datetime.now() - datetime.timedelta(days=kwargs['days_back']),
            datetime.datetime.now(),
        )

        for payment in payments:
            self.pair_payment(payment)

    def pair_payment(self, payment):
        if payment['amount'] < 0:
            return

        variable_symbol = payment['variable_symbol'] if 'variable_symbol' in payment else None
        order = None
        if variable_symbol:
            try:
                order = Order.objects.get(symvar=variable_symbol)
            except Order.DoesNotExist:
                order = None

        new_payment, created = OrderPayment.objects.get_or_create(
            ident=payment['transaction_id'],
            defaults={
                'amount': payment['amount'],
                'bank': payment['bank_name'],
                'currency': payment['currency'],
                'message': payment['recipient_message'],
                'order': order,
                'received_at': payment['date'],
                'sender': payment['account_number'],
                'status': 'paid',
                'symcon': payment['constant_symbol'],
                'symspc': payment['specific_symbol'],
                'symvar': variable_symbol,
                'user_identification': payment['user_identification'],
            },
        )
        if created and order:
            order.update_paid_status()
