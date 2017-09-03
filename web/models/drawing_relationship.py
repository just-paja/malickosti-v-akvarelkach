from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

DRAWING_RELATIONSHIP_TYPE_SIZE = 1
DRAWING_RELATIONSHIP_TYPE_DUPLICATE = 2

DRAWING_RELATIONSHIP_TYPE_CHOICES = (
    (
        DRAWING_RELATIONSHIP_TYPE_SIZE,
        _('Jiná velikost'),
    ),
    (
        DRAWING_RELATIONSHIP_TYPE_DUPLICATE,
        _('Duplikát'),
    ),
)


class DrawingRelationship(TimeStampedModel):
    parent = models.ForeignKey(
        'Drawing',
        related_name='drawings_child',
        help_text=_('Parent for this relationship. If you are not sure, \
         use object that is older.')
    )
    child = models.ForeignKey(
        'Drawing',
        related_name='drawings_parent',
        help_text=_('Child for this relationship. If you are not sure, \
         use object that is younger.')
        )
    kind = models.PositiveIntegerField(
        choices=DRAWING_RELATIONSHIP_TYPE_CHOICES,
    )

    class Meta:
        verbose_name = _('Drawing Relationship')
        verbose_name_plural = _('Drawing Relationships')

    def __str__(self):
        return self.name
