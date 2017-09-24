from django.forms import Form, CharField, EmailField, IntegerField
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
    customer_name = CharField(
        label=_('Celé jméno'),
        help_text=_('Vyplňte prosím vaše celé jméno'),
    )
    customer_email = EmailField(
        label=_('E-mail'),
        help_text=_('E-mail bude použit k zaslání potvrzení objednávky'),
    )
    customer_phone = CharField(
        label=_('Telefon'),
        help_text=_(
            'Telefonní číslo v mezinárodním tvaru, např: +420 123 456 789'
        ),
    )
    customer_address = CharField(
        label=_('Adresa'),
        help_text=_('Vyplňte prosím celou doručovací adresu'),
    )
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
            raise ValidationError(
                _('Neplatná kombinace metody doručení a platby.'),
            )

        return cleaned_data

    def get_value(self, key, *args):
        for source in args:
            if key in source:
                return str(source[key])
        return ''

    def get_values(self, order):
        if order:
            if 'delivery_method' in order and order['delivery_method']:
                delivery_method = order['delivery_method']
            else:
                delivery_method = DeliveryMethod.objects.get_default().id

            if 'payment_method' in order and order['payment_method']:
                payment_method = order['payment_method']
            else:
                payment_method = DeliveryMethod.objects.get(
                    id=delivery_method,
                ).get_default_payment().id
        else:
            delivery_method_default = DeliveryMethod.objects.get_default()
            delivery_method = delivery_method_default.id
            payment_method = delivery_method_default.get_default_payment().id

        return {
            'customer_name': self.get_value(
                'customer_name',
                self.data,
                order,
            ),
            'customer_email': self.get_value(
                'customer_email',
                self.data,
                order,
            ),
            'customer_phone': self.get_value(
                'customer_phone',
                self.data,
                order,
            ),
            'customer_address': self.get_value(
                'customer_address',
                self.data,
                order,
            ),
            'delivery_method': int(delivery_method),
            'payment_method': int(payment_method),
        }
