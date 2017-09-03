from datetime import datetime

from django.db.models import (
    CharField,
    ForeignKey,
    PositiveIntegerField,
    ImageField,
    ManyToManyField,
    Q,
)
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

DRAWING_STATUS_STORED = 1
DRAWING_STATUS_RESERVED = 2
DRAWING_STATUS_SOLD = 3

DRAWING_STATUS_CHOICES = (
    (DRAWING_STATUS_STORED, _('Aktuálně k prodeji')),
    (DRAWING_STATUS_RESERVED, _('Zarezervováno')),
    (DRAWING_STATUS_SOLD, _('Prodáno')),
)


class Drawing(TimeStampedModel):
    name = CharField(
        max_length=255,
        help_text=_(
            'Very short description that helps to recognize the object'
        ),
    )
    size = ForeignKey('DrawingSize')
    status = PositiveIntegerField(
        choices=DRAWING_STATUS_CHOICES,
        default=DRAWING_STATUS_STORED,
    )
    image = ImageField(
        verbose_name=_("Image of drawing"),
        height_field="image_height",
        width_field="image_width",
        upload_to='var/drawings',
    )
    image_height = PositiveIntegerField(null=True)
    image_width = PositiveIntegerField(null=True)
    price_levels = ManyToManyField('DrawingPriceLevel')

    class Meta:
        verbose_name = _('Drawing')
        verbose_name_plural = _('Drawings')

    def __str__(self):
        return self.name

    def get_active_price_level(self):
        now = datetime.now()
        self.price_levels.filter(
            Q(Q(valid_from__isnull=True) | Q(valid_from__gte=now)),
            Q(Q(valid_until__isnull=True) | Q(valid_until__lte=now)),
        ).order_by('-created').first()
