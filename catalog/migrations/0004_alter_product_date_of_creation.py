# Generated by Django 4.2.7 on 2023-12-23 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 1, 57, 26, 871118), verbose_name='Дата создания'),
        ),
    ]