from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    address = models.CharField(
        max_length=255,
        help_text=_('Address in human readable format'),
    )
    website = models.URLField(
        help_text=('Website URL'),
    )

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return self.name
