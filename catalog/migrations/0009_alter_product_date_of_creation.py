# Generated by Django 4.2.7 on 2024-01-14 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 16, 8, 38, 633628), verbose_name='Дата создания'),
        ),
    ]
