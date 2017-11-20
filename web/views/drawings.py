from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404

from drawings.models import (
    Drawing,
    DRAWING_AVAILABLE_STATES,
    DRAWING_STATUS_STORED,
    DRAWING_STATUS_RESERVED,
    DRAWING_STATUS_SOLD,
)


def view_drawings(request):
    drawings = Drawing.objects.filter(
        status__in=[DRAWING_STATUS_STORED, DRAWING_STATUS_RESERVED],
    ).order_by('status', 'name', '-created')
    return render(request, 'drawings/index.html', {
        'drawings': drawings,
    })


def view_drawings_sold(request):
    drawings = Drawing.objects.filter(
        status=DRAWING_STATUS_SOLD,
    )
    return render(request, 'drawings/index.html', {
        'drawings': drawings,
    })


def view_drawings_detail(request, id):
    try:
        drawing = Drawing.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'drawings/detail.html', {
        'available': drawing.status in DRAWING_AVAILABLE_STATES,
        'drawing': drawing,
        'in_cart': drawing.id in request.session.get('cart', []),
        'price': drawing.get_price(),
    })
