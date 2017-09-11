from django.shortcuts import render

from ..forms import OrderDelivery
from ..models import (
    Drawing,
    DeliveryMethod,
    PaymentMethod,
    VISIBILITY_PUBLIC,
)


def get_cart(request):
    return request.session.get('cart', [])


def view_order_delivery(request):
    if request.method == 'POST':
        formset = OrderDelivery(request.POST)
        if formset.is_valid():
            order = request.session.get('order', {})
            order['delivery_method'] = formset.cleaned_data.get('delivery_method')
            order['payment_method'] = formset.cleaned_data.get('payment_method')
    else:
        formset = OrderDelivery()

    cart = get_cart(request)
    drawings = Drawing.objects.filter(id__in=cart).all()
    price = 0

    for drawing in drawings:
        price += drawing.get_price()

    delivery_method_default = DeliveryMethod.objects.filter(
        visibility=VISIBILITY_PUBLIC,
    ).order_by('weight').first()

    payment_method_default = delivery_method_default.payment_methods.filter(
        visibility=VISIBILITY_PUBLIC,
    ).order_by('weight').first()

    return render(request, 'order/delivery.html', {
        'added': 'pridano' in request.GET,
        'delivery_methods': DeliveryMethod.objects.filter(visibility=VISIBILITY_PUBLIC),
        'value_delivery_method': int(formset.data.get(
            'delivery_method',
            delivery_method_default.id
        )),
        'value_payment_method': int(formset.data.get(
            'payment_method',
            payment_method_default.id
        )),
        'drawings': drawings,
        'empty': len(drawings) == 0,
        'formset': formset,
        'payment_methods': PaymentMethod.objects.filter(visibility=VISIBILITY_PUBLIC),
        'price': price,
        'purged': 'vyprazdneno' in request.GET,
        'removed': 'odebrano' in request.GET,
    })
