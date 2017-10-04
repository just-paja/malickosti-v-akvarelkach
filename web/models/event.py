from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .text_photo import TextPhoto
from .visibility import VisibilityField, VisibilityManager

EVENT_TYPE_EXPOSITION = 1
EVENT_TYPE_VERNISSAGE = 2

EVENT_TYPE_CHOICES = (
    (EVENT_TYPE_EXPOSITION, _('Výstava')),
    (EVENT_TYPE_VERNISSAGE, _('Vernisáž')),
)


class Event(TimeStampedModel):
    objects = VisibilityManager()
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    event_type = models.PositiveIntegerField(
        choices=EVENT_TYPE_CHOICES,
        default=EVENT_TYPE_EXPOSITION,
        verbose_name=_('Type'),
    )
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False)
    location = models.ForeignKey('Location')
    description = models.TextField(
        help_text=_(
            'Describe everything that user needs to know about this object.\
            You can format the text in Markdown'
        ),
    )
    visibility = VisibilityField()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return "%s: %s" % (self.get_type_name(), self.name)

    def get_type_name(self):
        for choice in EVENT_TYPE_CHOICES:
            if choice[0] == self.event_type:
                return choice[1]
        return ''


class EventPhoto(TextPhoto):
    event = models.ForeignKey(Event, related_name='photos')
