from django.urls import path
from django.contrib.auth.decorators import login_required

from products.views import PaymentView, ProductsView, CartView, AddCartView, RemoveCartView

urlpatterns = [
    path("", ProductsView.as_view(), name='products_index'),
    path('cart/', CartView.as_view(), name='cart'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('cart/add/<int:pk>/', AddCartView.as_view(), name='cart_add'),
    path('cart/remove/<int:pk>/', RemoveCartView.as_view(), name='cart_remove'),
]
