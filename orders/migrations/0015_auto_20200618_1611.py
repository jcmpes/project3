# Generated by Django 2.0.3 on 2020-06-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200618_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(max_length=5),
        ),
    ]