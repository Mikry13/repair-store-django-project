from django.contrib import admin

from app.admin import DefaultModelAdmin
from stock_orders.models import (
    SellerMarketplace,
    Seller,
    StockOrder,
    StockOrderItem,
)


@admin.register(SellerMarketplace)
class SellerMarketplaceAdmin(DefaultModelAdmin):
    pass


@admin.register(Seller)
class SellerAdmin(DefaultModelAdmin):
    pass


class StockOrderItemInline(admin.StackedInline):
    model = StockOrderItem
    extra = 0
    readonly_fields = ['total_price']


@admin.register(StockOrder)
class StockOrderAdmin(DefaultModelAdmin):
    list_display = ['order_date', 'seller']
    list_filter = ['seller']
    inlines = [StockOrderItemInline]


@admin.register(StockOrderItem)
class StockOrderItemAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'stock_order',
        'stock_item',
        'amount',
        'price',
        'shipping_price',
        'total_price',
        'currency',
    ]

    readonly_fields = ['total_price']
    fieldsets = (
        (None, {'fields': ('stock_order', 'stock_item', 'amount')}),
        ('Цены', {'fields': ('price', 'shipping_price', 'currency', 'total_price')}),
    )
