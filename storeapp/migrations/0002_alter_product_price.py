# Generated by Django 4.1.4 on 2023-01-30 04:51

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=6),
        ),
    ]
