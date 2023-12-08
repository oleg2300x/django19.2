from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Blogs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slag = models.CharField(max_length=255, verbose_name='Слаг')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'