from math import ceil

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

PAGE_SIZE = 20


def view_drawings(request):
    try:
        page = int(request.GET.get('stranka', 1))
    except ValueError:
        raise Http404

    for_sale = request.GET.get('prodejne', None)
    size_id = request.GET.get('velikost', None)
    sizes = DrawingSize.objects.all()
    drawings = Drawing.objects.filter(
        status__in=[DRAWING_STATUS_STORED, DRAWING_STATUS_RESERVED],
    )
    show_size = True
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

        show_size = False
        query_params['velikost'] = size.id
        drawings = drawings.filter(size=size_id)

    if page < 1:
        raise Http404

    start = (page - 1) * PAGE_SIZE
    end = (page - 1) * PAGE_SIZE + PAGE_SIZE
    items_total = drawings.count()
    drawings = drawings.order_by('status', 'name', '-created')[start:end]
    pages_total = ceil(items_total / PAGE_SIZE)

    return render(request, 'drawings/index.html', {
        'drawings': drawings,
        'items_total': items_total,
        'items_visible': len(drawings),
        'page_current': page,
        'page_next': page + 1,
        'page_prev': page - 1,
        'pages_total': pages_total,
        'pages': range(1, pages_total + 1),
        'per_page': PAGE_SIZE,
        'query_params': query_params,
        'show_size': show_size,
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
