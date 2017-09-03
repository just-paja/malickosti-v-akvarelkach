from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class DrawingSize(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    size_horizontal = models.PositiveIntegerField(
        help_text=_('How wide is the medium in milimeters'),
    )
    size_vertical = models.PositiveIntegerField(
        help_text=_('How tall is the medium in milimeters'),
    )

    class Meta:
        verbose_name = _('Drawing Size')
        verbose_name_plural = _('Drawing Sizes')

    def __str__(self):
        return self.name
