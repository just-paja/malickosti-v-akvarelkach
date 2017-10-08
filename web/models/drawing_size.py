from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class DrawingSize(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    size_horizontal = models.PositiveIntegerField(
        verbose_name=_('field-size-horizontal'),
        help_text=_('field-size-horizontal-help-text'),
    )
    size_vertical = models.PositiveIntegerField(
        verbose_name=_('field-size-vertical'),
        help_text=_('field-size-vertical-help-text'),
    )

    class Meta:
        verbose_name = _('Drawing Size')
        verbose_name_plural = _('Drawing Sizes')

    def __str__(self):
        return self.name
