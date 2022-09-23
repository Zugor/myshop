from django.shortcuts import render
from django.views import generic
from products.models import Products


# Create your views here.
class ProductsView(generic.ListView):
    model = Products

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user
        return context
