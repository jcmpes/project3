# Generated by Django 2.0.3 on 2020-06-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200617_0800'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DinnerPlatter',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.DeleteModel(
            name='RegularPizza',
        ),
        migrations.DeleteModel(
            name='Salad',
        ),
        migrations.DeleteModel(
            name='SicilianPizza',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default='large', max_length=5),
        ),
    ]
