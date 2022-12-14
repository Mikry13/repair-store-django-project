# Generated by Django 4.1 on 2022-09-25 22:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
                ('code', models.CharField(help_text='Код модели. Обычно находится у штрих-кода', max_length=64, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
                ('amount', models.PositiveIntegerField(help_text='>=1', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('state', models.CharField(choices=[('Новое', 'Новое'), ('Поставка', 'Поставка'), ('На складе', 'На складе'), ('Ремонтируется', 'Ремонтируется'), ('На продаже', 'На продаже'), ('Архив', 'Архив'), ('Проблемы после продажи', 'Post Selling Issues')], default='Новое', max_length=64, verbose_name='Статус')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.manufacturer', verbose_name='Производитель')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.itemmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Вещь на складе',
                'verbose_name_plural': 'Вещи на складе',
            },
        ),
        migrations.CreateModel(
            name='UniqueIdentifierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип уникального идентификатора',
                'verbose_name_plural': 'Типы уникальных идентификаторов',
            },
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Срок истечения')),
                ('initial_months_length', models.PositiveIntegerField(blank=True, help_text='>=1', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Изначальный размер гарантии')),
                ('store_warranty', models.BooleanField(verbose_name='Гарантия магазина')),
                ('description', models.TextField(verbose_name='Описание')),
                ('stock_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stock_items.stockitem', verbose_name='Вещь на складе')),
            ],
            options={
                'verbose_name': 'Гарантия',
                'verbose_name_plural': 'Гарантии',
            },
        ),
        migrations.CreateModel(
            name='UniqueIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256, verbose_name='Значение')),
                ('identifier_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.uniqueidentifiertype', verbose_name='Тип уникального идентификатора')),
                ('stock_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stock_items.stockitem', verbose_name='Вещь на складе')),
            ],
            options={
                'verbose_name': 'Уникальный идентификатор',
                'verbose_name_plural': 'Уникальные идентификаторы',
            },
        ),
        migrations.CreateModel(
            name='Repairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(help_text='>=1', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество использованных запчастей')),
                ('repair_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='in_use_repairs', to='stock_items.stockitem', verbose_name='Запчасть')),
                ('repairing_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repairs', to='stock_items.stockitem')),
            ],
            options={
                'verbose_name': 'Ремонт',
                'verbose_name_plural': 'Ремонты',
            },
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_items.manufacturer', verbose_name='Производитель'),
        ),
    ]
