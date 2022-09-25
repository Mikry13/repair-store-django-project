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


@admin.register(StockOrder)
class StockOrderAdmin(DefaultModelAdmin):
    pass


@admin.register(StockOrderItem)
class StockOrderItemAdmin(DefaultModelAdmin):
    pass
