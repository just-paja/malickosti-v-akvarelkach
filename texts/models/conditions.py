from django.db import models
from django.utils.translation import ugettext_lazy as _
from photos.models import Photo

from .text import Text


class ConditionsText(Text):

    class Meta:
        verbose_name = _('Trade Conditions')
        verbose_name_plural = _('Trade Conditions')


class ConditionsTextPhoto(Photo):
    text = models.ForeignKey('ConditionsText', related_name='photos')
