from django.db import models
from django.utils.translation import ugettext_lazy as _

VISIBILITY_PUBLIC = 1
VISIBILITY_PRIVATE = 2

VISIBILITY_CHOICES = (
    (VISIBILITY_PUBLIC, _('visibility-public')),
    (VISIBILITY_PRIVATE, _('visibility-private')),
)


class VisibilityField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        if 'default' in kwargs:
            del kwargs['default']

        if 'choices' in kwargs:
            del kwargs['choices']

        if 'verbose_name' in kwargs:
            del kwargs['verbose_name']

        super(VisibilityField, self).__init__(
            *args,
            **kwargs,
            choices=VISIBILITY_CHOICES,
            default=VISIBILITY_PUBLIC,
            verbose_name=_('field-visibility'),
        )


class VisibilityManager(models.Manager):
    def get_visible(self):
        return self.filter(visibility=VISIBILITY_PUBLIC)
