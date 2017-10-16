from django.contrib.admin import (
    ModelAdmin,
    register,
    StackedInline,
    TabularInline,
)
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
    OrderPayment,
    PaymentMethod,
    TextAbout,
    TextAboutPhoto,
    TextConditions,
    TextConditionsPhoto,
)


class PhotoAdmin(TabularInline):
    fields = ('image', 'description', 'weight')
    extra = 0
    ordering = ('-weight',)


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
        'price_levels',
    )
    search_fields = ['name', 'size__name', 'price_levels__price']


class EventPhotoAdmin(PhotoAdmin):
    model = EventPhoto


@register(Event)
class EventAdmin(ModelAdmin):
    inlines = [EventPhotoAdmin]
    list_display = (
        'name',
        'event_type',
        'start',
        'end',
        'all_day',
    )
    list_filter = (
        'event_type',
        'all_day',
    )
    search_fields = ['name']


class OrderDrawingAdmin(StackedInline):
    model = OrderDrawing
    readonly_fields = (
        'drawing',
    )
    extra = 0


payment_readonly_fields = (
    'ident',
    'symvar',
    'symcon',
    'symspc',
    'amount',
    'sender',
    'bank',
    'currency',
    'received_at',
    'user_identification',
)


@register(OrderPayment)
class OrderPaymentAdmin(ModelAdmin):
    model = OrderPayment
    list_display = (
        'id',
        'amount',
        'order',
        'sender',
        'bank',
        'symvar',
        'symcon',
        'created',
    )
    readonly_fields = payment_readonly_fields


class OrderPaymentInlineAdmin(StackedInline):
    model = OrderPayment
    readonly_fields = payment_readonly_fields
    extra = 0

    def has_delete_permission(self, request, id):
        return False


@register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [
        OrderDrawingAdmin,
        OrderPaymentInlineAdmin,
    ]
    list_display = (
        'symvar',
        'buyer',
        'status',
        'price',
        'paid',
        'over_paid',
        'delivery',
        'modified',
    )
    list_filter = (
        'status',
        'paid',
        'over_paid',
        'delivery',
    )
    readonly_fields = (
        'buyer',
        'price',
        'email',
        'phone',
        'paid',
        'over_paid',
    )
    search_fields = ['buyer', 'email', 'phone', 'items__drawing__name']


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
        'needs_account_info',
        'visibility',
    )


@register(Location)
class LocationAdmin(ModelAdmin):
    pass


class TextAdmin(ModelAdmin):
    list_display = (
        'name',
        'weight',
        'created',
        'modified',
    )
    ordering = ('-weight',)


class TextAboutPhotoAdmin(PhotoAdmin):
    model = TextAboutPhoto


@register(TextAbout)
class TextAboutAdmin(TextAdmin):
    inlines = [TextAboutPhotoAdmin]


class TextConditionsPhotoAdmin(PhotoAdmin):
    model = TextConditionsPhoto


@register(TextConditions)
class TextConditionsAdmin(TextAdmin):
    inlines = [TextConditionsPhotoAdmin]
