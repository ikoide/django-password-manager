from django.urls import path, include

from apps.accounts.views import RegistrationView, UserDeleteView

app_name = "accounts"

urlpatterns = [
    path("delete_account/", UserDeleteView.as_view(), name="delete_account"),
    path("", include("django.contrib.auth.urls")),
    path("register/", RegistrationView.as_view(), name="register")
]
