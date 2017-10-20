from django.contrib.admin import (
    ModelAdmin,
    register,
    TabularInline,
)
from .models import (
    Drawing,
    DrawingRelationship,
    DrawingSize,
)


class DrawingRelationshipAdmin(TabularInline):
    model = DrawingRelationship
    fk_name = 'parent'


@register(Drawing)
class DrawingAdmin(ModelAdmin):
    inlines = [DrawingRelationshipAdmin]
    fields = (
        'name',
        'size',
        'status',
        'image',
        'price_levels',
    )
    list_display = (
        'name',
        'size',
        'status',
    )
    readonly_fields = (
        'image_height',
        'image_width',
    )
    list_filter = (
        'size',
        'status',
    )
    search_fields = ['name', 'size__name', 'price_levels__price']


@register(DrawingSize)
class DrawingSizeAdmin(ModelAdmin):
    list_display = (
        'name',
        'size_horizontal',
        'size_vertical',
    )
