from django.forms import Form, IntegerField
from django.core.exceptions import (
    ObjectDoesNotExist,
    ValidationError,
)
from django.utils.translation import ugettext_lazy as _

from ..models import (
    DeliveryMethod,
    PaymentMethod,
)

def validate_id(value, model):
    try:
        model.objects.get(id=value)
    except ObjectDoesNotExist:
        raise ValidationError(_('Invalid Method'), params={
            'value': value,
        })

def validate_delivery_method(value):
    return validate_id(value, DeliveryMethod)

def validate_payment_method(value):
    return validate_id(value, PaymentMethod)


class DeliveryMethodField(IntegerField):
    default_validators = [validate_delivery_method]


class PaymentMethodField(IntegerField):
    default_validators = [validate_payment_method]


class OrderDelivery(Form):
    delivery_method = DeliveryMethodField()
    payment_method = PaymentMethodField()

    def clean(self):
        cleaned_data = super(OrderDelivery, self).clean()
        delivery_method_value = cleaned_data.get('delivery_method')
        payment_method_value = cleaned_data.get('payment_method')

        exists = DeliveryMethod.objects.filter(
            id=delivery_method_value,
            payment_methods__in=[payment_method_value]
        ).count()

        if not exists:
            raise ValidationError(_('Invalid combination of Delivery and Payment methods'))

        return cleaned_data
