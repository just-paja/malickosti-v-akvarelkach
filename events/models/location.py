from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    address = models.CharField(
        max_length=255,
        help_text=_('field-address-help-text'),
    )
    website = models.URLField(
        help_text=_('field-website-help-text'),
    )

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return self.name
