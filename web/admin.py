from django.contrib.admin import TabularInline, ModelAdmin, register
from .models import (
    DeliveryMethod,
    Drawing,
    DrawingPriceLevel,
    DrawingRelationship,
    DrawingSize,
    Event,
    Location,
    Order,
    OrderDrawing,
    PaymentMethod,
    TextAbout,
    TextAboutPhoto,
)


class DrawingRelationshipAdmin(TabularInline):
    model = DrawingRelationship
    fk_name = 'parent'


class OrderDrawingAdmin(TabularInline):
    model = OrderDrawing


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
    readonly_fields = (
        'image_height',
        'image_width',
    )


@register(Event)
class EventAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [OrderDrawingAdmin]


@register(DrawingPriceLevel)
class DrawingPriceLevelAdmin(ModelAdmin):
    pass


@register(DrawingSize)
class DrawingSizeAdmin(ModelAdmin):
    pass


@register(DeliveryMethod)
class DeliveryMethodAdmin(ModelAdmin):
    pass


@register(PaymentMethod)
class PaymentMethodAdmin(ModelAdmin):
    pass


@register(Location)
class LocationAdmin(ModelAdmin):
    pass


class TextAboutPhotoAdmin(TabularInline):
    model = TextAboutPhoto
    fields = ('image', 'description', 'weight')


@register(TextAbout)
class TextAboutAdmin(ModelAdmin):
    inlines = [TextAboutPhotoAdmin]
