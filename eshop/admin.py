from django.contrib.admin import (
    ModelAdmin,
    register,
    StackedInline,
)
from .models import (
    DeliveryMethod,
    Order,
    OrderDrawing,
    OrderPayment,
    PaymentMethod,
    PriceLevel,
)


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


@register(PriceLevel)
class PriceLevelAdmin(ModelAdmin):
    list_display = (
        'name',
        'price',
        'valid_from',
        'valid_until',
    )
    exclude = ('drawings',)


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
        'needs_account_info',
        'weight',
        'visibility',
    )
