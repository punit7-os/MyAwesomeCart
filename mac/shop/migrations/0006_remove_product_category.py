# Generated by Django 4.2.3 on 2023-09-06 16:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_remove_product_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
    ]
