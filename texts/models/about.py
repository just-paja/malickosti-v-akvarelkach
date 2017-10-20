from django.db import models
from django.utils.translation import ugettext_lazy as _
from photos.models import Photo

from .text import Text


class AboutText(Text):

    class Meta:
        verbose_name = _('About text')
        verbose_name_plural = _('About texts')


class AboutTextPhoto(Photo):
    text = models.ForeignKey('AboutText', related_name='photos')
