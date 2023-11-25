from django.db import models


NULLABLE = {'blank': True, 'null': True}
class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='Наименование категории')
    description_category = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category} - {self.description_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} ' \
               f'{self.price} {self.date_of_creation} {self.last_modified_date}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
