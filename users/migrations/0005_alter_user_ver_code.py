# Generated by Django 4.2.7 on 2024-01-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='749768566250', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
