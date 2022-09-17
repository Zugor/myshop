from django.contrib import admin

from products.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products, ProductsAdmin)