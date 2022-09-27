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
    search_fields = [
        'name',
        'manufacturer__name',
        'model__name',
    ]
    list_filter = [
        'manufacturer',
        'model',
    ]  # TODO: change model queryset by manufacturer
    autocomplete_fields = [
        'manufacturer',
        'model',
    ]


@admin.register(Repairs)
class RepairsAdmin(DefaultModelAdmin):
    search_fields = [
        'repairing_item__name',
        'repair_item__name',
    ]
    autocomplete_fields = [
        'repairing_item',
        'repair_item',
    ]


@admin.register(Manufacturer)
class ManufacturerAdmin(DefaultModelAdmin):
    search_fields = ['name']


@admin.register(ItemModel)
class ItemModelAdmin(DefaultModelAdmin):
    search_fields = [
        'name',
        'code',
        'manufacturer__name',
    ]
    list_filter = [
        'manufacturer',
    ]
    autocomplete_fields = [
        'manufacturer',
    ]


@admin.register(UniqueIdentifier)
class UniqueIdentifierAdmin(DefaultModelAdmin):
    search_fields = [
        'stock_item__name',
        'value',
        'identifier_type__name',
    ]
    list_filter = [
        'identifier_type',
    ]
    autocomplete_fields = [
        'stock_item',
        'identifier_type',
    ]


@admin.register(UniqueIdentifierType)
class UniqueIdentifierTypeAdmin(DefaultModelAdmin):
    search_fields = ['name']


@admin.register(Warranty)
class WarrantyAdmin(DefaultModelAdmin):
    search_fields = [
        'stock_item__name',
        'expiration_date',
        'initial_months_length',
    ]
    list_filter = [
        'store_warranty',
        # expired # TODO: add custom filter by 'expired'
    ]
    autocomplete_fields = [
        'stock_item',
    ]
