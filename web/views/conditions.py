from django.shortcuts import render

from ..models import (
    TextConditions,
)


def view_conditions(request):
    return render(request, 'conditions.html', {
        'conditions': TextConditions.objects.get_visible(),
    })
