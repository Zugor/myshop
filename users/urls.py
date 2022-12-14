from django.urls import path

from django.contrib.auth.views import LogoutView

from .views import login_view, register_user, LoginView

urlpatterns = [
    # path('login/', login_view, name="login"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name='logout'),
]
