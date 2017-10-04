from django.contrib.admin import TabularInline, ModelAdmin, register
from .models import (
    DeliveryMethod,
    Drawing,
    DrawingPriceLevel,
    DrawingRelationship,
    DrawingSize,
    Event,
    EventPhoto,
    Location,
    Order,
    OrderDrawing,
    PaymentMethod,
    TextAbout,
    TextAboutPhoto,
)


class PhotoAdmin(TabularInline):
    fields = ('image', 'description', 'weight')


class DrawingRelationshipAdmin(TabularInline):
    model = DrawingRelationship
    fk_name = 'parent'


class OrderDrawingAdmin(TabularInline):
    model = OrderDrawing
    readonly_fields = (
        'drawing',
    )


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


class EventPhotoAdmin(PhotoAdmin):
    model = EventPhoto


@register(Event)
class EventAdmin(ModelAdmin):
    inlines = [EventPhotoAdmin]


@register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [OrderDrawingAdmin]
    list_display = (
        'buyer',
        'status',
        'price',
        'delivery',
        'modified',
    )
    readonly_fields = (
        'buyer',
        'price',
        'email',
        'phone',
    )


@register(DrawingPriceLevel)
class DrawingPriceLevelAdmin(ModelAdmin):
    list_display = (
        'name',
        'price',
        'valid_from',
        'valid_until',
    )


@register(DrawingSize)
class DrawingSizeAdmin(ModelAdmin):
    list_display = (
        'name',
        'size_horizontal',
        'size_vertical',
    )


@register(DeliveryMethod)
class DeliveryMethodAdmin(ModelAdmin):
    list_display = (
        'name',
        'price',
        'weight',
        'visibility',
    )


@register(PaymentMethod)
class PaymentMethodAdmin(ModelAdmin):
    list_display = (
        'name',
        'price',
        'weight',
        'visibility',
    )

@register(Location)
class LocationAdmin(ModelAdmin):
    pass


class TextAboutPhotoAdmin(PhotoAdmin):
    model = TextAboutPhoto


@register(TextAbout)
class TextAboutAdmin(ModelAdmin):
    inlines = [TextAboutPhotoAdmin]
