from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .visibility import VisibilityField

class PaymentMethod(TimeStampedModel):
    name = models.CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    description = models.TextField(
        help_text=_(
            'Describe everything that user needs to know about this object.\
            You can format the text in Markdown'
        ),
    )
    price = models.PositiveIntegerField(
        default=0,
        help_text=_('This price will be added to Order in default currency'),
    )
    weight = models.PositiveIntegerField(
        default=0,
        help_text=_('More weight, more priority'),
    )
    visibility = VisibilityField()

    def __str__(self):
        return self.name
