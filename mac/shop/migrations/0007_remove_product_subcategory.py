# Generated by Django 4.2.3 on 2023-09-06 16:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_remove_product_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="subcategory",
        ),
    ]
