# Generated by Django 2.0.3 on 2020-06-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200613_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs',
            name='small',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
