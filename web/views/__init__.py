from .about import view_about
from .cart import (
    view_cart,
    view_cart_add_drawing,
    view_cart_purge,
    view_cart_remove_drawing,
)
from .contact import view_contact
from .drawings import (
    view_drawings,
    view_drawings_detail,
    view_drawings_sold,
)
from .events import view_events
from .home import view_home
from .orders import view_order_delivery

__all__ = (
    view_about,
    view_cart,
    view_cart_add_drawing,
    view_cart_purge,
    view_cart_remove_drawing,
    view_contact,
    view_drawings,
    view_drawings_detail,
    view_drawings_sold,
    view_events,
    view_home,
    view_order_delivery,
)
