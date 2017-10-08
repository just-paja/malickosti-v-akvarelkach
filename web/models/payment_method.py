from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .visibility import VisibilityField, VisibilityManager


class PaymentMethod(TimeStampedModel):
    objects = VisibilityManager()
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    description = models.TextField(
        help_text=_('field-description-help-text'),
    )
    needs_account_info = models.BooleanField(
        default=False,
        help_text=_('field-payment-method-need-account-info-help-text'),
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name=_('field-price'),
        help_text=_('field-method-price-help-text'),
    )
    weight = models.PositiveIntegerField(
        default=0,
        verbose_name=_('field-weight'),
        help_text=_('field-weight-help-text'),
    )
    visibility = VisibilityField()

    class Meta:
        verbose_name = _('Payment Method')
        verbose_name_plural = _('Payment Methods')

    def __str__(self):
        return self.name
