from django.contrib import admin

from app.admin import DefaultModelAdmin
from stock_items.models import (
    StockItem,
    Repairs,
    Manufacturer,
    ItemModel,
    UniqueIdentifier,
    UniqueIdentifierType,
    Warranty,
)


@admin.register(StockItem)
class StockItemAdmin(DefaultModelAdmin):
    pass


@admin.register(Repairs)
class RepairsAdmin(DefaultModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(DefaultModelAdmin):
    pass


@admin.register(ItemModel)
class ItemModelAdmin(DefaultModelAdmin):
    pass


@admin.register(UniqueIdentifier)
class UniqueIdentifierAdmin(DefaultModelAdmin):
    pass


@admin.register(UniqueIdentifierType)
class UniqueIdentifierTypeAdmin(DefaultModelAdmin):
    pass


@admin.register(Warranty)
class WarrantyAdmin(DefaultModelAdmin):
    pass
