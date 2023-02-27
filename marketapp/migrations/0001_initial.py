# Generated by Django 4.1.7 on 2023-02-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('image', models.TextField(max_length=1000, verbose_name='Фото товара')),
                ('category', models.CharField(choices=[('OTHER', 'Разное'), ('LAPTOP', 'Ноутбуки'), ('SMARTPHONES', 'Смартфоны'), ('FOR_KITCHEN', 'Техника для кухни')], default='OTHER', max_length=100, verbose_name='Категория')),
                ('in_stock', models.PositiveIntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость')),
            ],
        ),
    ]