# Generated by Django 5.0.2 on 2024-07-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_alter_shippingadress_shipping_adress2_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipped",
            field=models.BooleanField(default=False),
        ),
    ]