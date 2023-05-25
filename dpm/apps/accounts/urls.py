from django.urls import path, include

from apps.accounts.views import RegistrationView

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", RegistrationView.as_view(), name="register")
]
