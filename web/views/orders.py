from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse

from ..forms import OrderDelivery
from ..models import (
    Drawing,
    DeliveryMethod,
    PaymentMethod,
)


def get_cart(request):
    return request.session.get('cart', [])


def view_order_delivery(request):
    if request.method == 'POST':
        formset = OrderDelivery(request.POST)
        if formset.is_valid():
            print(formset.cleaned_data)
    else:
        formset = OrderDelivery()

    cart = get_cart(request)
    drawings = Drawing.objects.filter(id__in=cart).all()
    price = 0

    for drawing in drawings:
        price += drawing.get_price()

    return render(request, 'order/delivery.html', {
        'added': 'pridano' in request.GET,
        'drawings': drawings,
        'empty': len(drawings) == 0,
        'formset': formset,
        'price': price,
        'purged': 'vyprazdneno' in request.GET,
        'removed': 'odebrano' in request.GET,
        'payment_methods': PaymentMethod.objects.all(),
        'delivery_methods': DeliveryMethod.objects.all(),
    })
