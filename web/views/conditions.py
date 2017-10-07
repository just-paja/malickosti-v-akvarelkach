from django.shortcuts import render

from ..models import (
    TextConditions,
)


def view_conditions(request):
    try:
        conditions = TextConditions.objects.get_visible().order_by(
            '-created'
        )[0]
    except:
        conditions = None

    return render(request, 'conditions.html', {
        'conditions': conditions,
    })
