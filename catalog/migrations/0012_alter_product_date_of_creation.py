# Generated by Django 4.2.7 on 2024-01-14 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_product_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 14, 23, 12, 6, 625970), verbose_name='Дата создания'),
        ),
    ]
