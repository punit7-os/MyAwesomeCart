# Generated by Django 4.2.3 on 2023-09-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_product_category_product_image_product_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
