from django.conf import settings
from django.db import models
import datetime

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='Наименование категории')
    description_category = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата создания',)
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} ' \
               f'{self.price} {self.date_of_creation} {self.last_modified_date}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            (
                'product_published',
                'Can publish product'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='versions')
    version_number = models.CharField(max_length=150, verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='В наличии', default=True)

    def __str__(self):
        return f'{self.product} --> ({self.version_number} - {self.version_name})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'