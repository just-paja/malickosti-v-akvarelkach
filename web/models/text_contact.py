from django.db import models
from django.utils.translation import ugettext_lazy as _

from .text import Text
from .text_photo import TextPhoto


class TextContact(Text):

    class Meta:
        verbose_name = _('Text Contact')
        verbose_name_plural = _('Texts Contact')


class TextContactPhoto(TextPhoto):
    text = models.ForeignKey('TextContact', related_name='photos')
