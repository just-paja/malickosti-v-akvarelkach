from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class DrawingPriceLevel(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    price = models.PositiveIntegerField(
        help_text=_('This price will be added to Order in default currency'),
    )
    valid_from = models.DateField(null=True, blank=True)
    valid_until = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('Drawing Price Level')
        verbose_name_plural = _('Drawing Price Levels')

    def __str__(self):
        return self.name
