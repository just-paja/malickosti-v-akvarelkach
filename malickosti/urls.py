"""malickosti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from web.views import (
    view_about,
    view_cart,
    view_cart_add_drawing,
    view_cart_purge,
    view_cart_remove_drawing,
    view_order_confirm,
    view_order_confirmed,
    view_order_delivery,
    view_conditions,
    view_contact,
    view_drawings,
    view_drawings_detail,
    view_drawings_sold,
    view_events,
    view_events_archive,
    view_events_detail,
    view_home,
)

urlpatterns = [
    url(r'^$', view_home, name='home'),
    url(r'^o-mne$', view_about, name='about'),
    url(r'^kontakt$', view_contact, name='contact'),
    url(r'^obrazky$', view_drawings, name='drawings'),
    url(r'^obrazky/prodane$', view_drawings_sold, name='drawings-sold'),
    url(
        r'^obrazky/(?P<id>[0-9]+)$',
        view_drawings_detail,
        name='drawings-detail',
    ),
    url(
        r'^obrazky/(?P<id>[0-9]+)/replika$',
        view_contact,
        name='drawings-redraw',
    ),
    url(
        r'^obrazky/(?P<id>[0-9]+)/pridat-do-kosiku$',
        view_cart_add_drawing,
        name='drawings-cart-add',
    ),
    url(
        r'^kosik/odebrat-obrazek/(?P<id>[0-9]+)$',
        view_cart_remove_drawing,
        name='cart-remove-drawing',
    ),
    url(
        r'^kosik/objednavka/doruceni',
        view_order_delivery,
        name='order-delivery',
    ),
    url(
        r'^kosik/objednavka/potvrzeni',
        view_order_confirm,
        name='order-confirm',
    ),
    url(
        r'^kosik/objednavka/potvrzeno',
        view_order_confirmed,
        name='order-confirmed',
    ),
    url(r'^vystavy$', view_events, name='events'),
    url(r'^vystavy/archiv$', view_events_archive, name='events-archive'),
    url(r'^vystavy/(?P<id>[0-9]+)$', view_events_detail, name='events-detail'),
    url(r'^kosik/vyprazdnit$', view_cart_purge, name='cart-purge'),
    url(r'^kosik$', view_cart, name='cart'),
    url(r'^obchodni-podminky$', view_conditions, name='conditions'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
