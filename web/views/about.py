from django.shortcuts import render

from texts.models import AboutText


def view_about(request):
    return render(request, 'about.html', {
        'texts': AboutText.objects.get_visible(),
    })
