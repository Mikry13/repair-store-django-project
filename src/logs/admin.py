from django.contrib import admin

from app.admin import DefaultModelAdmin
from logs.models import (
    BuyerOrderLog,
    StockItemLog,
)


@admin.register(BuyerOrderLog)
class BuyerOrderLogAdmin(DefaultModelAdmin):
    autocomplete_fields = [
        'buyer_order',
    ]


@admin.register(StockItemLog)
class StockItemLogAdmin(DefaultModelAdmin):
    autocomplete_fields = [
        'stock_item',
    ]
