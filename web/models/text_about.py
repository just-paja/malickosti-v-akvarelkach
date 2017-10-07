from django.db import models
from django.utils.translation import ugettext_lazy as _

from .text import Text
from .text_photo import TextPhoto


class TextAbout(Text):

    class Meta:
        verbose_name = _('Text about')
        verbose_name_plural = _('Texts about')


class TextAboutPhoto(TextPhoto):
    text = models.ForeignKey('TextAbout', related_name='photos')
