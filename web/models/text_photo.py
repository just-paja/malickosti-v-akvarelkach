from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class TextPhoto(TimeStampedModel):
    image = models.ImageField(
        verbose_name=_("Image file"),
        height_field="height",
        width_field="width",
        upload_to='var/texts',
    )
    image_thumb_detail = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToFill(600, 600),
        ],
    )
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    description = models.TextField(
        help_text=_('You can format the text in Markdown'),
        null=True,
        blank=True,
    )
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('Text Photo')
        verbose_name_plural = _('Text Photos')
