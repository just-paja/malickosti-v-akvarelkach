from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class PriceLevel(TimeStampedModel):
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
    drawings = models.ManyToManyField(
        'eshop.PriceLevel',
        verbose_name=_('field-price-levels'),
        related_name='price_levels',
    )

    class Meta:
        verbose_name = _('Price Level')
        verbose_name_plural = _('Price Levels')

    def __str__(self):
        return self.name
