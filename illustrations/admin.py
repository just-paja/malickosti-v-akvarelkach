from django.contrib.admin import (
    ModelAdmin,
    register,
)
from .models import (
    HomepageIllustration,
)


class IllustrationAdmin(ModelAdmin):
    list_display = ('image_tag', 'position', 'weight')
    list_filter = (
        'position',
    )
    readonly_fields = ('image_tag', 'image_height', 'image_width')
    ordering = ('-weight',)


@register(HomepageIllustration)
class HomepageIllustrationAdmin(IllustrationAdmin):
    pass
