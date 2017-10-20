from datetime import datetime

from django.shortcuts import render
from django.http import Http404

from events.models import (
    Event,
    EVENT_TYPE_EXPOSITION,
)


def view_events(request):
    vernissages = Event.objects.get_visible().filter(
        start__gte=datetime.now(),
    ).exclude(event_type=EVENT_TYPE_EXPOSITION)
    expositions = Event.objects.get_visible().filter(
        event_type=EVENT_TYPE_EXPOSITION,
        start__gte=datetime.now(),
    )
    return render(request, 'events/index.html', {
        'expositions': expositions,
        'vernissages': vernissages,
    })


def view_events_archive(request):
    events = Event.objects.get_visible().filter(
        start__lt=datetime.now(),
    )
    return render(request, 'events/archive.html', {
        'events': events,
    })


def view_events_detail(request, id):
    event = Event.objects.get_visible().filter(id=id).first()

    if not event:
        raise Http404

    return render(request, 'events/detail.html', {
        'event': event,
        'photos': event.photos.all(),
    })
