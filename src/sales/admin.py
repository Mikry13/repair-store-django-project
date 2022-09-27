from django.contrib import admin

from app.admin import DefaultModelAdmin
from sales.models import (
    StoreItemMarketplace,
    StoreItem,
    StoreOrderItem,
    BuyerOrder,
    Buyer,
)


@admin.register(StoreItemMarketplace)
class StoreItemMarketplaceAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'name',
        'contacts',
    ]
    search_fields = [
        'name',
    ]


@admin.register(StoreItem)
class StoreItemAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'stock_item',
        'price',
        'currency',
        'marketplace',
    ]
    search_fields = [
        'stock_item__name',
    ]
    list_filter = [
        'marketplace',  # TODO: add custom filter gte lte price/currency
    ]
    autocomplete_fields = [
        'stock_item',
        'marketplace',
    ]


@admin.register(StoreOrderItem)
class StoreOrderItemAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'buyer_order',
        'store_item',
        'amount',
        'price',
        'currency',
        'total_price',
    ]
    readonly_fields = [
        'price',
        'currency',
        'total_price',
    ]

    search_fields = [
        'buyer_order__buyer__name',
        'store_item__stock_item__name',
    ]
    list_filter = [
        'store_item',
    ]
    autocomplete_fields = [
        'buyer_order',
        'store_item',
    ]

    fieldsets = (
        (None, {'fields': ('buyer_order', 'store_item', 'amount')}),
        ('Цены', {'fields': ('price', 'currency', 'total_price')}),
    )


class BuyerOrderInline(admin.StackedInline):
    model = StoreOrderItem
    extra = 0
    list_display = [
        'buyer_order',
        'store_item',
        'amount',
        'price',
        'currency',
        'total_price',
    ]
    readonly_fields = [
        'price',
        'currency',
        'total_price',
    ]

    search_fields = [
        'buyer_order__buyer__name',
        'store_item__stock_item__name',
    ]
    list_filter = [
        'store_item',
    ]
    autocomplete_fields = [
        'buyer_order',
        'store_item',
    ]


@admin.register(BuyerOrder)
class BuyerOrderAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'state',
        'buyer',
        'order_date',
        'ship_date',
        'shipment_address',
        'currency',
        'total_price',
    ]
    readonly_fields = [
        'total_price',
    ]
    search_fields = [
        'buyer__first_name',
        'buyer__middle_name',
        'buyer__last_name',
        'buyer__contacts',
        'order_date',
        'ship_date',
    ]
    list_filter = [
        'buyer',
    ]
    autocomplete_fields = [
        'buyer',
    ]
    inlines = [BuyerOrderInline]

    # TODO: gte lte by date.
    # TODO: search widget for filter values (can be too much lines)


@admin.register(Buyer)
class BuyerAdmin(DefaultModelAdmin):
    list_display = [
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'contacts',
    ]

    search_fields = [
        'first_name',
        'middle_name',
        'last_name',
        'contacts',
    ]
