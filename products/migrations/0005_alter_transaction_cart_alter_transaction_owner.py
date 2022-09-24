# Generated by Django 4.1.1 on 2022-09-24 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0004_transaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="cart",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.cart",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]