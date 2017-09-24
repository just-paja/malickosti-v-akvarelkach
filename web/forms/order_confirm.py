from django.conf import settings
from django.forms import Form, BooleanField
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField


class OrderConfirm(Form):
    captcha = ReCaptchaField(required=not settings.DEBUG)
    confirm_personal = BooleanField(
        label=_('Souhlasím se zpracováním osobních informací'),
    )
    confirm_rules = BooleanField(
        label=_('Souhlasím s podmínkami prodeje'),
    )
