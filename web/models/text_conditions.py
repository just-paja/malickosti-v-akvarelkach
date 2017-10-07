from django.db import models
from django.utils.translation import ugettext_lazy as _

from .text import Text
from .text_photo import TextPhoto


class TextConditions(Text):
    name = models.CharField(
        max_length=255,
        default='Obchodní podmínky',
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )

    class Meta:
        verbose_name = _('Trade Conditions')
        verbose_name_plural = _('Trade Conditions')


class TextConditionsPhoto(TextPhoto):
    text = models.ForeignKey('TextConditions')
