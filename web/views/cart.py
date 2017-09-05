from django.shortcuts import render, redirect
from django.http import Http404

from ..models import (
    Drawing,
    DRAWING_AVAILABLE_STATES,
)

def get_cart(request):
    return request.session.get('cart', [])


def view_cart(request):
    cart = get_cart(request)
    drawings = Drawing.objects.filter(id__in=cart).all()
    price = 0

    for drawing in drawings:
        price += drawing.get_price()

    return render(request, 'cart.html', {
        'drawings': drawings,
        'price': price,
    })


def view_cart_add_drawing(request, id):
    drawing = Drawing.objects.get(id=id)

    if not drawing:
        raise Http404

    if drawing.status not in DRAWING_AVAILABLE_STATES:
        raise Http404

    cart = get_cart(request)

    if drawing.id not in cart:
        cart.append(drawing.id)
        request.session['cart'] = cart

    return redirect('drawings-detail', id=id)
