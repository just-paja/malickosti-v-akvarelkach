from ..models import Drawing


def get_cart(request):
    cart = request.session.get('cart', [])
    price = Drawing.objects.get_price(cart)

    return {
        'cart': {
            'itemCount': len(cart),
            'itemIds': cart,
            'price': price,
        },
    }
