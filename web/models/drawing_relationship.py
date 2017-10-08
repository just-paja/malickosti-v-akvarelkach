from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

DRAWING_RELATIONSHIP_TYPE_SIZE = 1
DRAWING_RELATIONSHIP_TYPE_DUPLICATE = 2

DRAWING_RELATIONSHIP_TYPE_CHOICES = (
    (DRAWING_RELATIONSHIP_TYPE_SIZE, _('relationship-different-size')),
    (DRAWING_RELATIONSHIP_TYPE_DUPLICATE, _('relationship-duplicate')),
)


class DrawingRelationship(TimeStampedModel):
    parent = models.ForeignKey(
        'Drawing',
        related_name='drawings_child',
        verbose_name=_('field-drawing-child'),
        help_text=_('field-drawing-child-help-text'),
    )
    child = models.ForeignKey(
        'Drawing',
        related_name='drawings_parent',
        verbose_name=_('field-drawing-parent'),
        help_text=_('field-drawing-parent-help-text'),
    )
    kind = models.PositiveIntegerField(
        choices=DRAWING_RELATIONSHIP_TYPE_CHOICES,
    )

    class Meta:
        verbose_name = _('Drawing Relationship')
        verbose_name_plural = _('Drawing Relationships')

    def __str__(self):
        return self.name
