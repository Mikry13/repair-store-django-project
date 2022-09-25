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
    search_fields = ['name']
    list_filter = ['manufacturer', 'model']  # TODO: change model queryset by manufacturer


@admin.register(Repairs)
class RepairsAdmin(DefaultModelAdmin):
    search_fields = ['repairing_item__name', 'repair_item__name']


@admin.register(Manufacturer)
class ManufacturerAdmin(DefaultModelAdmin):
    pass


@admin.register(ItemModel)
class ItemModelAdmin(DefaultModelAdmin):
    search_fields = ['name']


@admin.register(UniqueIdentifier)
class UniqueIdentifierAdmin(DefaultModelAdmin):
    search_fields = ['stock_item__name', 'value']


@admin.register(UniqueIdentifierType)
class UniqueIdentifierTypeAdmin(DefaultModelAdmin):
    pass


# TODO: add custom filter by 'expired'
@admin.register(Warranty)
class WarrantyAdmin(DefaultModelAdmin):
    search_fields = ['stock_item__name']
