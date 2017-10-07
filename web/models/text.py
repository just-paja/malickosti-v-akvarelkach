from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .visibility import VisibilityField, VisibilityManager


class Text(TimeStampedModel):
    objects = VisibilityManager()
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    text = models.TextField(
        help_text=_('You can format the text in Markdown'),
    )
    visibility = VisibilityField()
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.name
