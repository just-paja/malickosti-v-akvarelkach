from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .visibility import VisibilityField, VisibilityManager


class DeliveryMethodManager(VisibilityManager):
    def get_default(self):
        return self.get_visible().order_by('weight').first()


class DeliveryMethod(TimeStampedModel):
    objects = DeliveryMethodManager()
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    description = models.TextField(
        help_text=_('field-description-help-text'),
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
    payment_methods = models.ManyToManyField('PaymentMethod')
    visibility = VisibilityField()

    class Meta:
        verbose_name = _('Delivery Method')
        verbose_name_plural = _('Delivery Methods')

    def __str__(self):
        return self.name

    def get_default_payment(self):
        return self.payment_methods.get_visible().order_by('weight').first()
