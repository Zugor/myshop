from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic, View
from django.http import Http404
from django.forms import ValidationError
from products.models import Product, Cart, AmountProductsCart, Transaction


# Create your views here.
class PaymentView(generic.CreateView):
    model = Transaction
    fields = ['address', 'phone']
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        user = self.request.user
        try:
            cart = Cart.objects.get(owner=user)
        except Cart.DoesNotExist:
            raise ValidationError('Cart does not exist!')
        form.instance.cart = cart
        form.instance.owner = user

        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     return super().post(request, *args, **kwargs)


class RemoveCartView(View):
    success_url = reverse_lazy('cart')

    def get(self, request, pk):
        user = request.user
        cart, created = Cart.objects.get_or_create(owner=user)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Http404('Product does not exist!')

        try:
            amount_product = AmountProductsCart.objects.get(product=product, owner=user)
        except AmountProductsCart.DoesNotExist:
            return Http404('Product does not exist in your cart!')
        cart.products.remove(amount_product)
        cart.save()

        return redirect(self.success_url)


class AddCartView(View):
    success_url = reverse_lazy('cart')

    def get(self, request, pk):
        user = request.user
        cart, created = Cart.objects.get_or_create(owner=user)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Http404('Product does not exist')

        amount_product, created = AmountProductsCart.objects.get_or_create(product=product, owner=user)
        amount_product.amount += 1
        amount_product.save()
        cart.products.add(amount_product)
        cart.save()

        return redirect(self.success_url)


class CartView(generic.ListView):
    model = Cart

    def get_queryset(self):
        queryset, created = self.model.objects.get_or_create(owner=self.request.user)

        return self.model.objects.filter(owner=self.request.user)


class ProductsView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user
        return context
