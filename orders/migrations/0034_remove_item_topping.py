# Generated by Django 2.0.3 on 2020-06-20 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0033_item_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='topping',
        ),
    ]
