from django.shortcuts import render

from ..models import TextAbout, VISIBILITY_PUBLIC


def view_about(request):
    texts = TextAbout.objects.filter(visibility=VISIBILITY_PUBLIC).order_by('-weight')
    return render(request, 'about.html', {
        'texts': texts,
    })
