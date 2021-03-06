# Generated by Django 2.0.3 on 2020-06-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200616_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('RP', 'Regular Pizza'), ('SP', 'Sicilian Pizza'), ('T', 'Topping'), ('S', 'Sub'), ('P', 'Pasta'), ('D', 'Dinner Platter'), ('Sa', 'Salad')], default='RP', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
