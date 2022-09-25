from app.base_config import AppConfig


class StockItemsConfig(AppConfig):
    name = 'stock_items'
    verbose_name = 'Склад' # FIXME: this might not be working in Django 4.1.0...
