# Generated by Django 4.1.1 on 2022-09-24 10:11

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_alter_transaction_cart_alter_transaction_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="phone",
            field=models.CharField(
                max_length=15, validators=[products.models.validate_phone]
            ),
        ),
    ]
