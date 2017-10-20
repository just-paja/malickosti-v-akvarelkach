from django.db import models
from django.utils.translation import ugettext_lazy as _
from photos.models import Photo

from .text import Text


class ContactText(Text):

    class Meta:
        verbose_name = _('Contact text')
        verbose_name_plural = _('Contact texts')


class ContactTextPhoto(Photo):
    text = models.ForeignKey('ContactText', related_name='photos')
