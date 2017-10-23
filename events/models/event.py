from datetime import datetime

from django.db.models import (
    BooleanField,
    DateTimeField,
    ForeignKey,
    CharField,
    TextField,
    PositiveIntegerField,
    Q,
)
from django.utils.translation import ugettext_lazy as _
from photos.models import Photo

from model_utils.models import TimeStampedModel

from visibility.models import VisibilityField, VisibilityManager

EVENT_TYPE_EXPOSITION = 1
EVENT_TYPE_VERNISSAGE = 2

EVENT_TYPE_CHOICES = (
    (EVENT_TYPE_EXPOSITION, _('type-exposition')),
    (EVENT_TYPE_VERNISSAGE, _('type-vernissage')),
)


class EventManager(VisibilityManager):
    def future(self):
        return self.get_visible().filter(
            Q(start__gte=datetime.now()) |
            Q(end__gte=datetime.now()),
        ).order_by('-start')

    def past(self):
        return self.get_visible().filter(
            Q(start__lt=datetime.now()) &
            Q(end__lt=datetime.now()),
        ).order_by('-start')


class Event(TimeStampedModel):
    objects = EventManager()
    name = CharField(
        max_length=255,
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    event_type = PositiveIntegerField(
        choices=EVENT_TYPE_CHOICES,
        default=EVENT_TYPE_EXPOSITION,
        verbose_name=_('Type'),
    )
    start = DateTimeField(
        verbose_name=_('field-start'),
    )
    end = DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('field-end'),
    )
    all_day = BooleanField(
        default=False,
        verbose_name=_('field-all-day'),
        help_text=_('field-all-day-help-text'),
    )
    location = ForeignKey('Location')
    description = TextField(
        help_text=_('field-description-help-text'),
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


class EventPhoto(Photo):
    event = ForeignKey(Event, related_name='photos')
