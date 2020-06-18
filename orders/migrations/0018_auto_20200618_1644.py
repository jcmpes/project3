# Generated by Django 2.0.3 on 2020-06-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_item_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, choices=[('LARGE', 'Large'), ('SMALL', 'Small')], max_length=5, null=True),
        ),
    ]
