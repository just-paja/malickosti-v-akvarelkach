from django.shortcuts import render

from drawings.models import Drawing
from events.models import Event


from illustrations.models import HomepageIllustration


def view_home(request):
    latest_drawings = Drawing.objects.get_available().order_by('-created')[:5]
    latest_events = Event.objects.future()[:5]
    illustrations = HomepageIllustration.objects.get_tuple()
    return render(request, 'home.html', {
        'illustrations': illustrations,
        'latest_drawings': latest_drawings,
        'latest_events': latest_events,
    })
