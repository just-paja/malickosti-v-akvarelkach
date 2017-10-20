from django.contrib.admin import (
    ModelAdmin,
    register,
    TabularInline,
)

from eshop.models import PriceLevel
from .models import (
    Drawing,
    DrawingRelationship,
    DrawingSize,
)


class DrawingRelationshipInline(TabularInline):
    model = DrawingRelationship
    fk_name = 'parent'
    extra = 0


class PriceLevelInline(TabularInline):
    model = PriceLevel.drawings.through
    extra = 1


@register(Drawing)
class DrawingAdmin(ModelAdmin):
    inlines = [
        PriceLevelInline,
        DrawingRelationshipInline
    ]
    fields = (
        'name',
        'size',
        'status',
        'image',
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
