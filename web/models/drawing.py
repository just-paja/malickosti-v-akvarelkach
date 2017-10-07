from datetime import datetime

from django.db.models import (
    CharField,
    ForeignKey,
    Manager,
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

DRAWING_AVAILABLE_STATES = [
    DRAWING_STATUS_STORED,
]


class DrawingManager(Manager):
    def get_available(self):
        return self.filter(status__in=DRAWING_AVAILABLE_STATES)

    def get_price(self, ids):
        drawings = self.filter(id__in=ids).all()
        price = 0
        for drawing in drawings:
            price += drawing.get_price()

        return price


class Drawing(TimeStampedModel):
    objects = DrawingManager()
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
        return '%s (%s)' % (self.name, self.size)

    def get_active_price_level(self):
        now = datetime.now()
        return self.price_levels.filter(
            (Q(valid_from__isnull=True) | Q(valid_from__gte=now)) &
            (Q(valid_until__isnull=True) | Q(valid_until__lte=now)),
        ).order_by('-created').first()

    def get_price(self):
        return self.get_active_price_level().price

    def is_price_visible(self):
        return self.status in DRAWING_AVAILABLE_STATES

    def is_status_visible(self):
        return self.status not in DRAWING_AVAILABLE_STATES
