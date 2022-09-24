from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=12)
    price = models.IntegerField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class AmountProductsCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    @property
    def get_price(self):
        return self.product.price * self.amount


class Cart(models.Model):
    products = models.ManyToManyField(AmountProductsCart)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def get_bill(self):
        my_bill = 0
        amount_products = self.products.all()
        for amount_product in amount_products:
            my_bill += amount_product.product.price * amount_product.amount
        # return sum([amount_product.product.price * amount_product.amount for amount_product in self.products])
        return my_bill
