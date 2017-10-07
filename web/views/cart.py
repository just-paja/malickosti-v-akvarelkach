from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse

from ..models import (
    Drawing,
    DRAWING_AVAILABLE_STATES,
)


def get_cart(request):
    return request.session.get('cart', [])


def view_cart(request):
    cart = get_cart(request)
    drawings = Drawing.objects.filter(id__in=cart).all()
    price = Drawing.objects.get_price(cart)

    return render(request, 'orders/cart.html', {
        'added': 'pridano' in request.GET,
        'drawings': drawings,
        'empty': len(drawings) == 0,
        'price': price,
        'purged': 'vyprazdneno' in request.GET,
        'removed': 'odebrano' in request.GET,
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
        return redirect(reverse('cart') + '?pridano')

    return redirect('drawings-detail', id=id)


def view_cart_remove_drawing(request, id):
    cart = get_cart(request)
    drawing_id = int(id)

    if drawing_id in cart:
        cart.remove(drawing_id)
        request.session['cart'] = cart

    return redirect(reverse('cart') + '?odebrano')


def view_cart_purge(request):
    request.session['cart'] = []
    return redirect(reverse('cart') + '?vyprazdneno')
