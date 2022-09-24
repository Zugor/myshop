from django.contrib import admin

from products.models import Product, Transaction


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('cart', 'address', 'phone', 'owner')


admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
