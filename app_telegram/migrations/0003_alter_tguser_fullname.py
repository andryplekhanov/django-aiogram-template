# Generated by Django 4.2.4 on 2023-08-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_telegram', '0002_callrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО в Telegram'),
        ),
    ]