from django.shortcuts import render

from ..models import TextAbout


def view_about(request):
    return render(request, 'about.html', {
        'texts': TextAbout.objects.get_visible(),
    })
