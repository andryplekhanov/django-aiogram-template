# Generated by Django 4.2.4 on 2023-08-09 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_telegram', '0003_alter_tguser_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='username',
        ),
        migrations.DeleteModel(
            name='CallRequest',
        ),
    ]