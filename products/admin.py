from django.contrib import admin

from products.models import Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


admin.site.register(Product, ProductsAdmin)
