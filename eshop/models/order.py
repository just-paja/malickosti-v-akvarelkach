from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import mail
from django.template.loader import render_to_string

from model_utils.models import TimeStampedModel

from .order_payment import STATUS_PAID

ORDER_STATUS_NEW = 1
ORDER_STATUS_CONFIRMED = 2
ORDER_STATUS_ON_ROUTE = 3
ORDER_STATUS_DELIVERED = 4
ORDER_STATUS_CANCELED = 5

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_NEW, _('status-new')),
    (ORDER_STATUS_CONFIRMED, _('status-confirmed')),
    (ORDER_STATUS_ON_ROUTE, _('status-on-route')),
    (ORDER_STATUS_DELIVERED, _('status-delivered')),
    (ORDER_STATUS_CANCELED, _('status-canceled')),
)


class Order(TimeStampedModel):
    buyer = models.CharField(
        max_length=255,
        verbose_name=_('field-buyer'),
        help_text=_('field-buyer-help-text'),
    )
    email = models.EmailField(
        verbose_name=_('field-email'),
    )
    phone = models.CharField(
        max_length=63,
        verbose_name=_('field-phone'),
    )
    address = models.CharField(
        max_length=63,
        verbose_name=_('field-address'),
        help_text=_('field-address-help-text'),
    )
    delivery = models.ForeignKey(
        'DeliveryMethod',
        verbose_name=_('field-delivery-method'),
    )
    payment = models.ForeignKey(
        'PaymentMethod',
        verbose_name=_('field-payment-method'),
    )
    price = models.PositiveIntegerField(
        verbose_name=_('field-price'),
    )
    paid = models.BooleanField(
        default=False,
        verbose_name=_('field-paid'),
    )
    over_paid = models.BooleanField(
        default=False,
        verbose_name=_('field-over-paid'),
    )
    symvar = models.CharField(
        verbose_name=_("field-symvar"),
        max_length=63,
        blank=True,
        unique=True,
    )
    status = models.PositiveIntegerField(
        choices=ORDER_STATUS_CHOICES,
        default=ORDER_STATUS_NEW,
        verbose_name=_('field-status'),
    )

    initial_paid = False
    initial_status = None

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_paid = self.paid
        self.initial_over_paid = self.over_paid
        self.initial_status = self.status

    def __str__(self):
        return '%s %s' % (_('Order'), self.symvar)

    def generate_symvar(self):
        """Generate variable symbol for a new order."""
        today = datetime.now().strftime('%Y')
        top = Order.objects.order_by('-id').first()

        if top:
            total = int(top.symvar.split(today)[-1]) + 1
        else:
            total = 1

        self.symvar = "%s%s" % (today, total)

    def notify_accepted(self):
        self.notify(
            settings.EMAIL_MANAGER,
            'Vytvořena objednávka %s' % self.symvar,
            render_to_string('mail/order-manager-notify.txt', {
                'order': self,
            }),
        )
        self.notify(
            self.email,
            'Objednávka %s: Přijato' % self.symvar,
            render_to_string('mail/order-accepted.txt', {
                'order': self,
            }),
        )

    def notify_on_route(self):
        self.notify(
            self.email,
            'Objednávka %s odeslána' % self.symvar,
            render_to_string('mail/order-on-route.txt', {
                'order': self,
            }),
        )

    def notify_underpaid(self):
        self.notify(
            self.email,
            'Objednávka %s: Nedoplatek' % self.symvar,
            render_to_string('mail/order-underpaid.txt', {
                'order': self,
                'payments': self.payments.all(),
                'amount_to_pay': self.price - self.get_total_amount_received()
            }),
        )

    def notify_paid(self):
        self.notify(
            self.email,
            'Objednávka %s zaplacena' % self.symvar,
            render_to_string('mail/order-paid.txt', {
                'order': self,
                'payments': self.payments.all(),
                'amount_to_pay': abs(
                    self.price -
                    self.get_total_amount_received()
                ),
            }),
        )

    def notify_canceled(self):
        self.notify(
            self.email,
            'Objednávka %s zrušena' % self.symvar,
            render_to_string('mail/order-canceled.txt', {
                'order': self,
            }),
        )

    def notify_current_status(self):
        if self.status == ORDER_STATUS_NEW:
            self.notify_accepted()
        elif self.status == ORDER_STATUS_ON_ROUTE:
            self.notify_on_route()
        elif self.status == ORDER_STATUS_CANCELED:
            self.notify_canceled()

    def notify(self, rcpt, subject, body):
        mail.send_mail(
            subject,
            body,
            settings.EMAIL_ORDER_SENDER,
            [rcpt],
        )

    def save(self, *args, **kwargs):
        if not self.symvar:
            self.generate_symvar()

        super().save(*args, **kwargs)

        if self.initial_paid != self.paid and self.paid:
            self.mark_drawings_as_sold()

        if self.initial_status != self.status:
            self.notify_current_status()

    def get_total_amount_received(self):
        paid = (
            self.payments
                .filter(status=STATUS_PAID)
                .aggregate(total=models.Sum('amount'))
        )
        return paid['total'] if paid['total'] else 0

    def update_paid_status(self):
        paid_price = self.get_total_amount_received()
        self.paid = paid_price >= self.price
        self.over_paid = paid_price > self.price
        self.save()

        if self.paid:
            if not self.initial_paid:
                self.notify_paid()
        else:
            self.notify_underpaid()

    def mark_drawings_as_sold(self):
        for item in self.items.all():
            item.mark_as_sold()
