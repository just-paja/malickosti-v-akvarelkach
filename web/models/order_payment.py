"""Payment model."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

STATUS_IN_PROGRESS = 1
STATUS_PAID = 2
STATUS_CANCELED = 3

STATUS_CHOICES = (
    (STATUS_IN_PROGRESS, _('status-in-progress')),
    (STATUS_PAID, _('status-paid')),
    (STATUS_CANCELED, _('status-canceled')),
)


class OrderPayment(TimeStampedModel):
    """Stores payments."""

    order = models.ForeignKey(
        'Order',
        blank=True,
        null=True,
        verbose_name=_("Order"),
        help_text=_("Which order is this payment related to?"),
        related_name='payments',
    )
    ident = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("field-payment-ident"),
        help_text=_("field-payment-ident-help-text"),
    )
    symvar = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("field-symvar"),
    )
    symcon = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("field-symcon"),
    )
    symspc = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("field-symspc"),
    )
    amount = models.CharField(
        max_length=255,
        verbose_name=_("field-amount"),
    )
    sender = models.CharField(
        max_length=255,
        blank=True,
        default='unknown',
        verbose_name=_("field-payment-sender"),
        help_text=_("field-payment-sender-help-text"),
    )
    bank = models.CharField(
        max_length=255,
        blank=True,
        default='unknown',
        verbose_name=_("Bank"),
    )
    currency = models.CharField(
        max_length=255,
        blank=True,
        default='unknown',
        verbose_name=_("field-currency"),
    )
    received_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("field-received-at"),
        help_text=_("field-received-at-help-text"),
    )
    message = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("field-message"),
    )
    status = models.PositiveIntegerField(
        default=STATUS_PAID,
        choices=STATUS_CHOICES,
        verbose_name=_('field-status'),
    )
    user_identification = models.CharField(
        blank=True,
        null=True,
        verbose_name=_("field-user-identification"),
        help_text=_("field-user-identification-help-text"),
        max_length=255,
    )

    class Meta:
        verbose_name = _('Order Payment')
        verbose_name_plural = _('Order Payments')

    def __str__(self):
        """Return name as string representation."""
        return "Payment from %s" % self.received_at

    def save(self, *args, **kwargs):
        """Update order when paid."""
        super().save(*args, **kwargs)

        if self.order:
            self.order.update_paid_status()
