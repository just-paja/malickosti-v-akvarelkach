from datetime import datetime

from django.conf import settings
from django.db.models import (
    ForeignKey,
    CharField,
    ImageField,
    Manager,
    ManyToManyField,
    PositiveIntegerField,
    Q,
)
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from model_utils.models import TimeStampedModel

from .watermark import Watermark

DRAWING_STATUS_STORED = 1
DRAWING_STATUS_RESERVED = 2
DRAWING_STATUS_SOLD = 3

DRAWING_STATUS_CHOICES = (
    (DRAWING_STATUS_STORED, _('status-for-sale')),
    (DRAWING_STATUS_RESERVED, _('status-reserved')),
    (DRAWING_STATUS_SOLD, _('status-sold')),
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
        verbose_name=_('field-name'),
        help_text=_('field-name-help-text'),
    )
    size = ForeignKey(
        'DrawingSize',
        related_name='drawings',
        verbose_name=_('field-size'),
    )
    status = PositiveIntegerField(
        choices=DRAWING_STATUS_CHOICES,
        default=DRAWING_STATUS_STORED,
        verbose_name=_('field-drawing-status'),
    )
    image = ImageField(
        height_field="image_height",
        upload_to='var/drawings',
        verbose_name=_("field-drawing-image"),
        width_field="image_width",
    )
    image_thumb_detail = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToFill(600, 600),
            Watermark(
                '%s/web/static/images/watermark-black.png' % settings.BASE_DIR,
                0.09,
            )
        ],
    )
    image_thumb_list = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToFill(300, 300),
            Watermark(
                '%s/web/static/images/watermark-white.png' % settings.BASE_DIR,
                0.1,
            ),
        ],
    )
    image_height = PositiveIntegerField(null=True)
    image_width = PositiveIntegerField(null=True)
    price_levels = ManyToManyField(
        'DrawingPriceLevel',
        verbose_name=_('field-price-levels'),
    )

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
