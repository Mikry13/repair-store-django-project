from django.contrib import admin

from app.admin import DefaultModelAdmin
from logs.models import (
    BuyerOrderLog,
    StockItemLog,
)


@admin.register(BuyerOrderLog)
class BuyerOrderLogAdmin(DefaultModelAdmin):
    pass


@admin.register(StockItemLog)
class StockItemLogAdmin(DefaultModelAdmin):
    pass
