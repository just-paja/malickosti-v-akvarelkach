from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404

from drawings.models import (
    Drawing,
    DrawingSize,
    DRAWING_AVAILABLE_STATES,
    DRAWING_STATUS_STORED,
    DRAWING_STATUS_RESERVED,
    DRAWING_STATUS_SOLD,
)


def view_drawings(request):
    for_sale = request.GET.get('prodejne', None)
    size_id = request.GET.get('velikost', None)
    sizes = DrawingSize.objects.all()
    drawings = Drawing.objects.filter(
        status__in=[DRAWING_STATUS_STORED, DRAWING_STATUS_RESERVED],
    )
    query_params = {}

    if for_sale and for_sale == 'ne':
        query_params['prodejne'] = 'ne'
        drawings = Drawing.objects.filter(
            status=DRAWING_STATUS_SOLD,
        )

    if size_id:
        try:
            size = DrawingSize.objects.get(pk=size_id)
        except ObjectDoesNotExist:
            raise Http404

        query_params['velikost'] = size.id
        drawings = drawings.filter(size=size_id)

    drawings = drawings.order_by('status', 'name', '-created')

    return render(request, 'drawings/index.html', {
        'drawings': drawings,
        'query_params': query_params,
        'sizes': sizes,
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
