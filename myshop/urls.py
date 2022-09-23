from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import ProductsView

urlpatterns = [
                  path("", ProductsView.as_view(), name='index'),
                  path("admin/", admin.site.urls),
                  path("products/", include("products.urls")),
                  path("users/", include("users.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://github.com/Zugor/myshop
