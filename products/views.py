from django.shortcuts import render
from django.views import generic
from products.models import Products

# Create your views here.
class ProductsView(generic.ListView):
    model = Products