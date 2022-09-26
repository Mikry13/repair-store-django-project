# Generated by Django 4.1 on 2022-09-26 02:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock_items', '0002_WarrantyDescription_isNull'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('contacts', models.TextField(verbose_name='Контактные данные')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='BuyerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('Рубли', 'Рубли'), ('Tether', 'Tether')], default='Рубли', max_length=64, verbose_name='Валюта')),
                ('total_price', models.FloatField(editable=False, verbose_name='Суммарная цена')),
                ('order_date', models.DateTimeField(verbose_name='Дата/Время заказа')),
                ('ship_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата/Время получения заказа покупателем')),
                ('shipment_address', models.CharField(blank=True, max_length=128, null=True, verbose_name='Адрес доставки')),
                ('state', models.CharField(choices=[('Новый', 'Новый'), ('Ожидает отправки', 'Ожидает отправки'), ('Доставляется', 'Доставляется'), ('Доставлено', 'Доставлено'), ('Имеет проблемы', 'Имеет проблемы')], default='Новый', max_length=64, verbose_name='Статус')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.buyer', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ покупателя',
                'verbose_name_plural': 'Заказы покупателей',
            },
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена продажи')),
                ('currency', models.CharField(choices=[('Рубли', 'Рубли'), ('Tether', 'Tether')], default='Рубли', max_length=64, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Вещь в продаже',
                'verbose_name_plural': 'Вещи в продаже',
            },
        ),
        migrations.CreateModel(
            name='StoreItemMarketplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('contacts', models.TextField(help_text='site, or address', verbose_name='Контактные данные')),
            ],
            options={
                'verbose_name': 'Торговая площадка',
                'verbose_name_plural': 'Торговые площадки',
            },
        ),
        migrations.CreateModel(
            name='StoreOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(help_text='>=1', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('price', models.FloatField(editable=False, null=True, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('Рубли', 'Рубли'), ('Tether', 'Tether')], default='Рубли', editable=False, max_length=64, null=True, verbose_name='Валюта')),
                ('total_price', models.FloatField(editable=False, null=True, verbose_name='Суммарная цена')),
                ('buyer_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.buyerorder', verbose_name='Заказ покупателя')),
                ('store_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.storeitem', verbose_name='Вещь в магазине')),
            ],
            options={
                'verbose_name': 'Позиция заказа покупателя',
                'verbose_name_plural': 'Позиции заказа покупателя',
            },
        ),
        migrations.AddField(
            model_name='storeitem',
            name='marketplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.storeitemmarketplace', verbose_name='Площадка для продажи'),
        ),
        migrations.AddField(
            model_name='storeitem',
            name='stock_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.stockitem', verbose_name='Вещь на складе'),
        ),
    ]
