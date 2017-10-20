from django.utils.translation import ugettext_lazy as _

from django.db.models import ImageField, Manager, PositiveIntegerField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from model_utils.models import TimeStampedModel


ILLUSTRATION_POSITION_LEFT = 1
ILLUSTRATION_POSITION_CENTER = 2
ILLUSTRATION_POSITION_RIGHT = 3

ILLUSTRATION_POSITION_CHOICES = [
    (ILLUSTRATION_POSITION_LEFT, _('position_left')),
    (ILLUSTRATION_POSITION_CENTER, _('position_center')),
    (ILLUSTRATION_POSITION_RIGHT, _('position_right')),
]


class IllustrationManager(Manager):
    def get_tuple(self):
        drawings = []
        drawings.append(self.filter(position=ILLUSTRATION_POSITION_LEFT).first())
        drawings.append(self.filter(position=ILLUSTRATION_POSITION_CENTER).first())
        drawings.append(self.filter(position=ILLUSTRATION_POSITION_RIGHT).first())
        return [drawing for drawing in drawings if drawing]


class Illustration(TimeStampedModel):
    objects = IllustrationManager()
    image = ImageField(
        height_field="image_height",
        upload_to='var/illustration',
        verbose_name=_("field-drawing-image"),
        width_field="image_width",
    )
    position = PositiveIntegerField(choices=ILLUSTRATION_POSITION_CHOICES)
    weight = PositiveIntegerField(default=0)
    image_thumb_detail = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToFill(300, 300),
        ],
    )
    image_thumb_admin = ImageSpecField(
        source='image',
        format='JPEG',
        options={'quality': 95},
        processors=[
            ResizeToFill(100, 100),
        ],
    )
    image_height = PositiveIntegerField(null=True)
    image_width = PositiveIntegerField(null=True)

    class Meta:
        abstract = True
        verbose_name = _('Illustration')
        verbose_name_plural = _('Illustrations')

    def image_tag(self):
        return u'<img src="%s" />' % self.image_thumb_admin.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
