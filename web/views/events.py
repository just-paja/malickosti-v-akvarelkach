from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404

from events.models import (
    Event,
    EVENT_TYPE_EXPOSITION,
)


def view_events(request):
    vernissages = Event.objects.future().exclude(event_type=EVENT_TYPE_EXPOSITION)
    expositions = Event.objects.future().filter(event_type=EVENT_TYPE_EXPOSITION)
    return render(request, 'events/index.html', {
        'expositions': expositions,
        'vernissages': vernissages,
    })


def view_events_archive(request):
    events = Event.objects.past()
    return render(request, 'events/archive.html', {
        'events': events,
    })


def view_events_detail(request, id):
    try:
        event = Event.objects.get_visible().filter(id=id).first()
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'events/detail.html', {
        'event': event,
        'photos': event.photos.all(),
    })
