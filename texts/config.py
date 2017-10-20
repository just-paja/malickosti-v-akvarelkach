from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TextsConfig(AppConfig):
    name = 'texts'
    verbose_name = _('Texts')
