# Generated by Django 3.0.7 on 2020-06-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20200619_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='Item', to='orders.Topping'),
        ),
    ]
