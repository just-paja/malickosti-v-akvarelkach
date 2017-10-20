from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class DrawingTag(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )

    class Meta:
        verbose_name = _('Drawing Tag')
        verbose_name_plural = _('Drawing Tags')

    def __str__(self):
        return self.name
