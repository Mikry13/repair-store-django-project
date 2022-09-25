from django.core.validators import MinValueValidator
from django.db import models

from app.models import DefaultModel


class SellerMarketplace(DefaultModel):
    name = models.CharField('Наименование', max_length=64)
    contacts = models.TextField('Контактные данные')

    class Meta:
        verbose_name = 'Торговая площадка'
        verbose_name_plural = 'Торговые площадки'


class Seller(DefaultModel):
    name = models.CharField('Наименование', max_length=64)
    contacts = models.TextField('Контактные данные')
    marketplace = models.ForeignKey('stock_orders.SellerMarketplace', verbose_name='Торговая площадка', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class StockOrder(DefaultModel):
    seller = models.ForeignKey('stock_orders.Seller', verbose_name='Продавец', on_delete=models.PROTECT)
    order_date = models.DateTimeField('Дата/Время заказа')

    def __str__(self) -> str:
        return f'{self.seller.name} | {self.order_date}'

    class Meta:
        verbose_name = 'Закупка'
        verbose_name_plural = 'Закупки'


class StockOrderItem(DefaultModel):
    class Currency(models.TextChoices):
        RUB = 'Рубли'
        USD = 'Доллары'
        EUR = 'Евро'
        YEN = 'Йены'
        YUAN = 'Юань'

    stock_order = models.ForeignKey('stock_orders.StockOrder', verbose_name='Закупка', on_delete=models.CASCADE)
    stock_item = models.ForeignKey('stock_items.StockItem', verbose_name='Вещь на складе', on_delete=models.PROTECT)

    amount = models.FloatField('Количество', help_text='>=1', validators=[MinValueValidator(1)])
    price = models.FloatField('Цена за штуку')
    shipping_price = models.FloatField('Цена доставки', null=True, blank=True)
    total_price = models.FloatField('Суммарная цена')

    currency = models.CharField('Валюта', max_length=64, choices=Currency.choices, default=Currency.RUB)

    def calculate_total_price(self):
        self.total_price = self.amount * self.price + (self.shipping_price if self.shipping_price else 0.0)

    def __str__(self) -> str:
        return f'{self.stock_order} | {self.stock_item}'

    class Meta:
        verbose_name = 'Позиция закупки'
        verbose_name_plural = 'Позиции закупок'
