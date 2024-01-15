# Generated by Django 4.2.7 on 2023-12-23 19:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 5, 56, 58, 930877), verbose_name='Дата создания'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(blank=True, max_length=150, null=True, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='В наличии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
