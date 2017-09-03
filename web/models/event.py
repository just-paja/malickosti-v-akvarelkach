from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

EVENT_TYPE_EXPOSITION = 1
EVENT_TYPE_VERNISSAGE = 2

EVENT_TYPE_CHOICES = (
    (EVENT_TYPE_EXPOSITION, _('Výstava')),
    (EVENT_TYPE_VERNISSAGE, _('Vernisáž')),
)


class Event(TimeStampedModel):
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
    start_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField()
    end_time = models.TimeField(null=True, blank=True)
    location = models.ForeignKey('Location')
    description = models.TextField(
        help_text=_(
            'Describe everything that user needs to know about this object.\
            You can format the text in Markdown'
        ),
    )

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
