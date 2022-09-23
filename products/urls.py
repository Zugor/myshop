from django.urls import path
from django.contrib.auth.decorators import login_required

from products.views import ProductsView

urlpatterns = [
    path("", ProductsView.as_view()),
]
