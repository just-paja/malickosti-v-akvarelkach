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
from .events import (
    view_events,
    view_events_archive,
    view_events_detail,
)
from .home import view_home
from .orders import (
    view_order_confirm,
    view_order_confirmed,
    view_order_delivery,
)

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
    view_events_archive,
    view_events_detail,
    view_home,
    view_order_confirm,
    view_order_confirmed,
    view_order_delivery,
)
