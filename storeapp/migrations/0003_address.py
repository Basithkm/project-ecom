# Generated by Django 4.1.4 on 2023-01-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('town', models.TextField()),
                ('street', models.TextField()),
                ('landmark', models.TextField()),
            ],
        ),
    ]
