# Generated by Django 2.0.3 on 2020-06-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200616_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
        ),
    ]
