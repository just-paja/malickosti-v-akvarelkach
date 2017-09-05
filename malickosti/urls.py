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
from django.contrib import admin
from django.views.static import serve
from web.views import (
    view_about,
    view_cart,
    view_cart_add_drawing,
    view_contact,
    view_drawings,
    view_drawings_detail,
    view_drawings_sold,
    view_events,
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
        r'^obrazky/(?P<id>[0-9]+)/pridat-do-kosiku$',
        view_cart_add_drawing,
        name='drawings-cart-add',
    ),
    url(r'^udalosti$', view_events, name='events'),
    url(r'^kosik$', view_cart, name='cart'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(
            r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT},
        ),
    ]
