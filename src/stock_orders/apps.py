from app.base_config import AppConfig


class StockOrdersConfig(AppConfig):
    name = 'stock_orders'
    verbose_name = 'Закупки'  # FIXME: this might not be working in Django 4.1.0...
