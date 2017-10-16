from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from ..forms import OrderConfirm, OrderDelivery
from ..models import (
    Drawing,
    DeliveryMethod,
    Order,
    PaymentMethod,
)


def get_cart(request):
    return request.session.get('cart', [])


def get_order(request):
    return request.session.get('order', {})


def save_order(request, order, form_data):
    order['delivery_method'] = form_data.get('delivery_method')
    order['payment_method'] = form_data.get('payment_method')
    order['customer_address'] = form_data.get('customer_address')
    order['customer_name'] = form_data.get('customer_name')
    order['customer_email'] = form_data.get('customer_email')
    order['customer_phone'] = form_data.get('customer_phone')
    request.session['order'] = order


def view_order_delivery(request):
    cart = get_cart(request)
    order = get_order(request)

    if len(cart) == 0:
        return redirect(reverse('cart'))

    if request.method == 'POST':
        form = OrderDelivery(request.POST)
        if form.is_valid():
            save_order(request, order, form.cleaned_data)
            return redirect(reverse('order-confirm'))
    else:
        form = OrderDelivery(initial=order)

    drawings = Drawing.objects.filter(id__in=cart).all()
    price = Drawing.objects.get_price(cart)

    return render(request, 'orders/delivery.html', {
        'delivery_methods': DeliveryMethod.objects.get_visible(),
        'drawings': drawings,
        'form': form,
        'form_data': form.get_values(order),
        'payment_methods': PaymentMethod.objects.get_visible(),
        'price': price,
    })


def view_order_confirm(request):
    cart = get_cart(request)
    order = get_order(request)

    if len(cart) == 0:
        return redirect(reverse('cart'))

    drawings = Drawing.objects.filter(id__in=cart).all()
    delivery_method = DeliveryMethod.objects.get(
        id=order.get('delivery_method'),
    )
    payment_method = delivery_method.payment_methods.get(
        id=order.get('payment_method')
    )
    price = (
        Drawing.objects.get_price(cart) +
        delivery_method.price +
        payment_method.price
    )

    if request.method == 'POST':
        form = OrderConfirm(request.POST)
        if form.is_valid():
            order_saved = Order.objects.create(
                address=order['customer_address'],
                buyer=order['customer_name'],
                delivery=delivery_method,
                email=order['customer_email'],
                payment=payment_method,
                phone=order['customer_phone'],
                price=price,
            )

            for drawing in drawings:
                order_saved.items.create(drawing=drawing)
                drawing.mark_as_reserved()
                drawing.save()

            request.session['cart'] = []
            request.session['order_confirmed'] = order_saved.id
            return redirect(reverse('order-confirmed'))
    else:
        form = OrderConfirm()

    return render(request, 'orders/confirm.html', {
        'delivery_method': delivery_method,
        'drawings': drawings,
        'form': form,
        'order': order,
        'payment_method': payment_method,
        'price': price,
    })


def view_order_confirmed(request):
    order_id = request.session['order_confirmed']

    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'orders/confirmed.html', {
        'order': order,
    })
