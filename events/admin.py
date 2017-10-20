from django.contrib.admin import ModelAdmin, register
from photos.admin import PhotoAdmin

from .models import (
    Event,
    EventPhoto,
    Location,
)


class EventPhotoAdmin(PhotoAdmin):
    model = EventPhoto


@register(Event)
class EventAdmin(ModelAdmin):
    inlines = [EventPhotoAdmin]
    list_display = (
        'name',
        'event_type',
        'start',
        'end',
        'all_day',
    )
    list_filter = (
        'event_type',
        'all_day',
    )
    search_fields = ['name']


@register(Location)
class LocationAdmin(ModelAdmin):
    pass
