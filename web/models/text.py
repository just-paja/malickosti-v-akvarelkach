from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .visibility import VisibilityField, VisibilityManager


class TextManager(VisibilityManager):
    def get_visible(self):
        return super().get_visible().order_by('-weight')


class Text(TimeStampedModel):
    objects = TextManager()
    name = models.CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    text = models.TextField(
        help_text=_('field-text-help-text'),
    )
    visibility = VisibilityField()
    weight = models.PositiveIntegerField(
        default=0,
        verbose_name=_('field-weight'),
        help_text=_('field-weight-help-text'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.name

    def get_photos(self):
        return self.photos.order_by('-weight')
