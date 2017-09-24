from django.shortcuts import render
from ..models import (
    Drawing,
)


def view_home(request):
    latest = Drawing.objects.get_available().order_by('created')[:5]
    return render(request, 'home.html', {
        'latest_drawings': latest,
    })
