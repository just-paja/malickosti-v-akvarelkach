from django.conf import settings
from django.forms import Form, CharField, EmailField
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField


class ContactForm(Form):
    contact_name = CharField(
        label=_('field-contact-name'),
    )
    contact_email = EmailField(
        label=_('field-contact-email'),
    )
    contact_message = CharField(
        label=_('field-contact-message'),
    )
    captcha = ReCaptchaField(required=not settings.DEBUG)
