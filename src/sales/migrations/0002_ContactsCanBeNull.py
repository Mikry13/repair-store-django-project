# Generated by Django 4.1.1 on 2022-09-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitemmarketplace',
            name='contacts',
            field=models.TextField(blank=True, help_text='site, or address', null=True, verbose_name='Контактные данные'),
        ),
    ]
