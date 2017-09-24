from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

ORDER_STATUS_NEW = 1
ORDER_STATUS_CONFIRMED = 2
ORDER_STATUS_ON_ROUTE = 3
ORDER_STATUS_DELIVERED = 4
ORDER_STATUS_CANCELED = 5

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS_NEW, _('Nová')),
    (ORDER_STATUS_CONFIRMED, _('Potvrzená')),
    (ORDER_STATUS_ON_ROUTE, _('Na cestě')),
    (ORDER_STATUS_DELIVERED, _('Doručená')),
    (ORDER_STATUS_CANCELED, _('Zrušená')),
)


class Order(TimeStampedModel):
    buyer = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=63)
    address = models.CharField(max_length=63)
    delivery = models.ForeignKey('DeliveryMethod')
    payment = models.ForeignKey('PaymentMethod')
    price = models.PositiveIntegerField()
    status = models.PositiveIntegerField(
        choices=ORDER_STATUS_CHOICES,
        default=ORDER_STATUS_NEW,
    )
