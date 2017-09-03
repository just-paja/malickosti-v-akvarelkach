from django.shortcuts import render
from django.http import Http404

from ..models import (
    Drawing,
    DRAWING_STATUS_STORED,
    DRAWING_STATUS_RESERVED,
    DRAWING_STATUS_SOLD,
)


def view_drawings(request):
    drawings = Drawing.objects.filter(
        status__in=[DRAWING_STATUS_STORED, DRAWING_STATUS_RESERVED],
    )
    return render(request, 'drawings.html', {
        'drawings': drawings,
    })


def view_drawings_sold(request):
    drawings = Drawing.objects.filter(
        status=DRAWING_STATUS_SOLD,
    )
    return render(request, 'drawings.html', {
        'drawings': drawings,
    })


def view_drawings_detail(request, id):
    drawing = Drawing.objects.get(id=id)

    if not drawing:
        raise Http404

    return render(request, 'drawings-detail.html', {
        'drawing': drawing,
        'price': drawing.get_price(),
    })
