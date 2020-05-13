from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'ordered', 'quantity']
    list_filter = ['ordered']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'being_delivered',
                    'received', 'refund_requested', 'refund_granted', 'user',
                    'shipping_address', 'billing_address', 'payment', 'coupon']

    list_display_links = ['user', 'shipping_address',
                          'billing_address', 'payment', 'coupon']

    list_filter = ['ordered', 'being_delivered', 'received',
                   'refund_requested', 'refund_granted', 'start_date', 'ordered_date']

    search_fields = [
        'user__username',
        'ref_code',
    ]

    list_editable = ['refund_granted']
