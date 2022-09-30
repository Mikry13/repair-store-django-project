from django.contrib import admin

from stock_items.models import StockItem
from stock_orders.models import StockOrder


class StockItemModelByManufacturer(admin.SimpleListFilter):
    title = 'Модели выбранного производителя'
    parameter_name = 'model__id__exact'

    def lookups(self, request, model_admin):
        if 'manufacturer__id__exact' not in request.GET:
            return None
        _id = request.GET['manufacturer__id__exact']

        stock_items_model = model_admin.model
        stock_items = set([item for item in stock_items_model.objects.filter(model__manufacturer__id=_id)])

        unique_lookups = {item.model.id: item.model.name for item in stock_items}
        return [(key, unique_lookups[key]) for key in unique_lookups]

    def queryset(self, request, queryset):
        if 'model__id__exact' in request.GET:
            _id = request.GET['model__id__exact']
            return queryset.filter(model__id__exact=_id)
        elif self.value():
            return queryset.filter(manufacturer__id__exact=self.value())


class StockItemByOrder(admin.SimpleListFilter):
    title = 'По закупке'
    parameter_name = 'order__id__exact'

    def lookups(self, request, model_admin):
        queryset = model_admin.model.objects.all()
        if 'manufacturer__id__exact' in request.GET:
            queryset = queryset.filter(manufacturer__id__exact=request.GET.get('manufacturer__id__exact'))
        if 'model__id__exact' in request.GET:
            queryset = queryset.filter(model__id__exact=request.GET.get('model__id__exact'))

        orders = StockOrder.objects.filter(
            stockorderitem__stock_item__pk__in=[
                model.id for model in queryset
            ]
        )

        unique_lookups = {order.id: order.order_date for order in orders}
        return [(key, unique_lookups[key]) for key in unique_lookups]

    def queryset(self, request, queryset):
        if 'order__id__exact' in request.GET:
            return queryset.filter(stockorderitem__stock_order__id__exact=request.GET.get('order__id__exact'))

        elif self.value():
            return queryset


class StockItemByStockOrderBySeller(admin.SimpleListFilter):
    title = 'Продавец'
    parameter_name = 'seller__id__exact'

    def lookups(self, request, model_admin):
        return None
    def queryset(self, request, queryset):
        return queryset