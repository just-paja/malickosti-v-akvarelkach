from ..models import Drawing

def get_cart(request):
    cart = request.session.get('cart', [])
    price = 0

    for drawingId in cart:
        price += Drawing.objects.get(id=drawingId).get_price()

    return {
        'cart': {
            'itemCount': len(cart),
            'itemIds': cart,
            'price': price,
        },
    }
