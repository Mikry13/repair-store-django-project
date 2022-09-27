from django.core.validators import MinValueValidator
from django.db import models
from app.models import DefaultModel


# TODO: add logging for status change (status changed to ...)
# TODO: amount logic referred to orders/repairs/selling
class StockItem(DefaultModel):
    class STATUS(models.TextChoices):
        NEW = 'Новое', 'Новое'
        SHIPPING = 'Поставка', 'Поставка'
        IN_STOCK = 'На складе', 'На складе'
        REPAIRING = 'Ремонтируется', 'Ремонтируется'
        IN_STORE = 'На продаже', 'На продаже'
        ARCHIVE = 'Архив', 'Архив'
        POST_SELLING_ISSUES = 'Проблемы после продажи'

    name = models.CharField('Наименование', max_length=128)
    manufacturer = models.ForeignKey('stock_items.Manufacturer', verbose_name='Производитель', on_delete=models.PROTECT)
    model = models.ForeignKey('stock_items.ItemModel', verbose_name='Модель', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество', help_text='>=1', validators=[MinValueValidator(1)])
    state = models.CharField('Статус', max_length=64, choices=STATUS.choices, default=STATUS.NEW)

    def __str__(self) -> str:
        return f'{self.name} #{self.id} | left: {self.amount} | state: {self.state}'

    class Meta:
        verbose_name = 'Вещь на складе'
        verbose_name_plural = 'Вещи на складе'


# TODO: add logging for StockItem (used x<amount> of <repair_item> #<repair_item.id> for <repairing_item>)
# TODO: add delete signal
class Repairs(DefaultModel):
    repairing_item = models.ForeignKey('stock_items.StockItem', related_name='repairs', on_delete=models.CASCADE)
    repair_item = models.ForeignKey('stock_items.StockItem', related_name='in_use_repairs', verbose_name='Запчасть', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField('Количество использованных запчастей', help_text='>=1', validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return f'#{self.repair_item.id} {self.repair_item.name}' \
               f' -> ' \
               f'#{self.repairing_item.id} {self.repairing_item.name}'

    class Meta:
        verbose_name = 'Ремонт'
        verbose_name_plural = 'Ремонты'


class Manufacturer(DefaultModel):
    name = models.CharField('Наименование', max_length=64)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class ItemModel(DefaultModel):
    name = models.CharField('Наименование', max_length=64)
    code = models.CharField('Код', max_length=64, help_text='Код модели. Обычно находится у штрих-кода')
    manufacturer = models.ForeignKey('stock_items.Manufacturer', verbose_name='Производитель', on_delete=models.PROTECT)
    notes = models.TextField('Заметки', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name} | {self.code}'

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


# TODO: add logging for StockItem (Related UniqueIdentifier <id> is created. Value: <value>)
# TODO: add logging for StockItem (Related UniqueIdentifier <id> is changed. New Value: <value>)
# TODO: add logging for StockItem (Related UniqueIdentifier <id> is deleted.)
class UniqueIdentifier(DefaultModel):
    stock_item = models.OneToOneField('stock_items.StockItem', verbose_name='Вещь на складе', on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=256)
    identifier_type = models.ForeignKey('stock_items.UniqueIdentifierType', verbose_name='Тип уникального идентификатора', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.value

    class Meta:
        verbose_name = 'Уникальный идентификатор'
        verbose_name_plural = 'Уникальные идентификаторы'


class UniqueIdentifierType(DefaultModel):
    name = models.CharField('Наименование', max_length=128)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Тип уникального идентификатора'
        verbose_name_plural = 'Типы уникальных идентификаторов'


# TODO: add logging for StockItem (Added Warranty #<id>. <Expiration date: <date> if <expiration_date> else Initial Length: <initial_months_length>
# TODO: add logging for StockItem (Warranty's #<id> length/store_warranty/expiration_date is changed)
class Warranty(DefaultModel):
    stock_item = models.OneToOneField('stock_items.StockItem', verbose_name='Вещь на складе', on_delete=models.CASCADE)
    expiration_date = models.DateField('Срок истечения', null=True, blank=True)
    initial_months_length = models.PositiveIntegerField('Изначальный размер гарантии', help_text='>=1', validators=[MinValueValidator(1)], null=True, blank=True)
    store_warranty = models.BooleanField('Гарантия магазина')
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self) -> str:
        return f'#{self.stock_item.id} | {self.stock_item.name}'

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантии'
