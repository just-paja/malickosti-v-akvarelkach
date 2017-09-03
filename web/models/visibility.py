from django.db import models
from django.utils.translation import ugettext_lazy as _

VISIBILITY_PUBLIC = 1
VISIBILITY_PRIVATE = 2

VISIBILITY_CHOICES = (
    (VISIBILITY_PUBLIC, _('Public')),
    (VISIBILITY_PRIVATE, _('Hidden')),
)


class VisibilityField(models.PositiveIntegerField):
    def __init__(self, *args, **kwargs):
        if 'default' in kwargs:
            del kwargs['default']

        if 'choices' in kwargs:
            del kwargs['choices']

        super(VisibilityField, self).__init__(
            *args,
            **kwargs,
            choices=VISIBILITY_CHOICES,
            default=VISIBILITY_PUBLIC,
        )
