# Generated by Django 4.2.7 on 2024-01-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='322723910387', max_length=15, verbose_name='Проверочный код'),
        ),
    ]