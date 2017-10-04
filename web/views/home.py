from datetime import datetime

from django.shortcuts import render

from ..models import (
    Drawing,
    Event,
)


def view_home(request):
    latest_drawings = Drawing.objects.get_available().order_by('-created')[:5]
    latest_events = Event.objects.get_visible().filter(
        start__gte=datetime.now(),
    ).order_by('-start')[:5]
    return render(request, 'home.html', {
        'latest_drawings': latest_drawings,
        'latest_events': latest_events,
    })
