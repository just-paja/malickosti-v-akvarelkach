from django.utils.translation import ugettext_lazy as _

from .illustration import Illustration


class HomepageIllustration(Illustration):
    class Meta:
        verbose_name = _('Homepage illustration')
        verbose_name_plural = _('Homepage illustrations')
