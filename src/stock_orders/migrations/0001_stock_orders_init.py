# Generated by Django 4.1 on 2022-09-25 19:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock_items', '0003_stock_orders_init'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('contacts', models.TextField(verbose_name='Контактные данные')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
            },
        ),
        migrations.CreateModel(
            name='SellerMarketplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('contacts', models.TextField(verbose_name='Контактные данные')),
            ],
            options={
                'verbose_name': 'Торговая площадка',
                'verbose_name_plural': 'Торговые площадки',
            },
        ),
        migrations.CreateModel(
            name='StockOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(verbose_name='Дата/Время заказа')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_orders.seller', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Закупка',
                'verbose_name_plural': 'Закупки',
            },
        ),
        migrations.CreateModel(
            name='StockOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(help_text='>=1', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Цена за штуку')),
                ('shipping_price', models.FloatField(blank=True, null=True, verbose_name='Цена доставки')),
                ('total_price', models.FloatField(verbose_name='Суммарная цена')),
                ('currency', models.CharField(choices=[('Рубли', 'Rub'), ('Доллары', 'Usd'), ('Евро', 'Eur'), ('Йены', 'Yen'), ('Юань', 'Yuan')], default='Рубли', max_length=64, verbose_name='Валюта')),
                ('stock_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.stockitem', verbose_name='Вещь на складе')),
                ('stock_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_orders.stockorder', verbose_name='Закупка')),
            ],
            options={
                'verbose_name': 'Позиция закупки',
                'verbose_name_plural': 'Позиции закупок',
            },
        ),
        migrations.AddField(
            model_name='seller',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_orders.sellermarketplace', verbose_name='Торговая площадка'),
        ),
    ]