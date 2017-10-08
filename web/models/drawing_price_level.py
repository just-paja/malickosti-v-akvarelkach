from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class DrawingPriceLevel(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    price = models.PositiveIntegerField(
        verbose_name=_('field-price'),
        help_text=_('field-method-price-help-text'),
    )
    valid_from = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('field-valid-from'),
    )
    valid_until = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('field-valid-until'),
    )

    class Meta:
        verbose_name = _('Drawing Price Level')
        verbose_name_plural = _('Drawing Price Levels')

    def __str__(self):
        return self.name
