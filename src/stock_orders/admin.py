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
    search_fields = [
        'name',
    ]


@admin.register(Seller)
class SellerAdmin(DefaultModelAdmin):
    search_fields = [
        'name',
        'marketplace__name',
    ]
    autocomplete_fields = [
        'marketplace'
    ]


class StockOrderItemInline(admin.StackedInline):
    model = StockOrderItem
    extra = 0
    readonly_fields = [
        'total_price',
    ]


@admin.register(StockOrder)
class StockOrderAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'order_date',
        'seller',
    ]
    search_fields = [
        'order_date',
        'seller__name',
    ]
    list_filter = [
        'seller',
    ]
    autocomplete_fields = [
        'seller',
    ]
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

    readonly_fields = [
        'total_price',
    ]
    autocomplete_fields = [
        'stock_order',
        'stock_item',
    ]

    fieldsets = (
        (None, {'fields': ('stock_order', 'stock_item', 'amount')}),
        ('Цены', {'fields': ('price', 'shipping_price', 'currency', 'total_price')}),
    )
