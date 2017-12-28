from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToCover


class Photo(TimeStampedModel):
    image = models.ImageField(
        verbose_name=_("field-image"),
        height_field="height",
        width_field="width",
        upload_to='var/texts',
    )
    image_thumb_detail = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToCover(600, 600),
        ],
    )
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    description = models.TextField(
        help_text=_('field-text-help-text'),
        null=True,
        blank=True,
    )
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
