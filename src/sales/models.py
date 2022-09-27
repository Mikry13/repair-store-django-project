from django.core.validators import MinValueValidator
from django.db import models

from app.models import DefaultModel


class StoreItemMarketplace(DefaultModel):
    name = models.CharField('Наименование', max_length=64)
    contacts = models.TextField('Контактные данные', help_text='site, or address', null=True, blank=True)

    class Meta:
        verbose_name = 'Торговая площадка'
        verbose_name_plural = 'Торговые площадки'


# TODO: add 'reserved for store amount' field and logic
# TODO: add 'is archive' boolean field and logic
class StoreItem(DefaultModel):
    class Currency(models.TextChoices):
        RUB = 'Рубли', 'Рубли'
        USDT = 'Tether', 'Tether'

    stock_item = models.ForeignKey('stock_items.StockItem', verbose_name='Вещь на складе', on_delete=models.PROTECT)
    price = models.FloatField('Цена продажи')
    currency = models.CharField('Валюта', max_length=64, choices=Currency.choices, default=Currency.RUB)
    marketplace = models.ForeignKey('sales.StoreItemMarketplace', verbose_name='Площадка для продажи', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.stock_item}'

    class Meta:
        verbose_name = 'Вещь в продаже'
        verbose_name_plural = 'Вещи в продаже'


class StoreOrderItem(DefaultModel):
    buyer_order = models.ForeignKey('sales.BuyerOrder', verbose_name='Заказ покупателя', on_delete=models.CASCADE)
    store_item = models.ForeignKey('sales.StoreItem', verbose_name='Вещь в магазине', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество', help_text='>=1', validators=[MinValueValidator(1)])

    price = models.FloatField('Цена', editable=False, null=True)
    currency = models.CharField('Валюта', max_length=64, choices=StoreItem.Currency.choices, default=StoreItem.Currency.RUB, null=True, editable=False)
    total_price = models.FloatField('Суммарная цена', editable=False, null=True)

    def calculate_amount(self) -> None:
        if self.amount > self.store_item.stock_item.amount:
            self.amount = self.store_item.stock_item.amount

    def calculate_price(self) -> None:
        if not self.price:
            self.price = self.store_item.price

    def calculate_total_price(self) -> None:
        self.total_price = self.store_item.price * self.amount

    def calculate_currency(self) -> None:
        if not self.currency:
            self.currency = self.store_item.currency

    def __str__(self) -> str:
        return f'{self.store_item} x{self.amount}'

    class Meta:
        verbose_name = 'Позиция заказа покупателя'
        verbose_name_plural = 'Позиции заказа покупателя'


# TODO: post_save signal or smth to update update stock amount when state is set from NEW to PENDING
# TODO: convert prices from one to another based on order currency
# FIXME: post_save signal for StockOrderItem to update total price, or it needs two saves to calculate.
class BuyerOrder(DefaultModel):
    class STATUS(models.TextChoices):
        NEW = 'Новый', 'Новый'
        PENDING = 'Ожидает отправки', 'Ожидает отправки'
        SHIPPING = 'Доставляется', 'Доставляется'
        SHIPPED = 'Доставлено', 'Доставлено'
        HAVE_ISSUES = 'Имеет проблемы', 'Имеет проблемы'

    buyer = models.ForeignKey('sales.Buyer', verbose_name='Покупатель', on_delete=models.CASCADE)
    currency = models.CharField('Валюта', max_length=64, choices=StoreItem.Currency.choices, default=StoreItem.Currency.RUB)
    total_price = models.FloatField('Суммарная цена', editable=False)

    order_date = models.DateTimeField('Дата/Время заказа')
    ship_date = models.DateTimeField('Дата/Время получения заказа покупателем', null=True, blank=True)
    shipment_address = models.CharField('Адрес доставки', max_length=128, null=True, blank=True)

    state = models.CharField('Статус', max_length=64, choices=STATUS.choices, default=STATUS.NEW)

    def calculate_total_price(self) -> None:  # NOTE: temporary solution, will switch to signals
        order_items = StoreOrderItem.objects.filter(buyer_order__id=self.id).values('total_price', 'currency')
        self.total_price = sum([order_item['total_price'] for order_item in order_items])  # NOTE: temporary solution

    def __str__(self) -> str:
        return f'{"(доставлен)" if self.state == self.STATUS.SHIPPED else ""}' \
               f'{self.buyer} | {self.order_date}'

    class Meta:
        verbose_name = 'Заказ покупателя'
        verbose_name_plural = 'Заказы покупателей'


class Buyer(DefaultModel):
    first_name = models.CharField('Имя', max_length=150)
    middle_name = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    last_name = models.CharField('Отчество', max_length=150, null=True, blank=True)
    contacts = models.TextField('Контактные данные')

    @property
    def full_name(self) -> str:
        return f'{self.last_name if self.last_name else ""}' \
               f' {self.first_name}' \
               f' {self.middle_name if self.middle_name else ""}'

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
