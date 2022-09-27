from django.db import models

from app.models import DefaultModel


class DefaultLog(DefaultModel):
    event = models.CharField('Событие', max_length=128)
    description = models.TextField('Описание')
    timestamp = models.DateTimeField('timestamp')

    class Meta:
        abstract = True


class BuyerOrderLog(DefaultLog):
    buyer_order = models.ForeignKey('sales.BuyerOrder', verbose_name='Заказ покупателя', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'История заказа покупателя'
        verbose_name_plural = 'Истории заказов покупателей'


class StockItemLog(DefaultLog):
    stock_item = models.ForeignKey('stock_items.StockItem', verbose_name='Вещь на складе', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'История вещи на складе'
        verbose_name_plural = 'Истории вещей на складе'
