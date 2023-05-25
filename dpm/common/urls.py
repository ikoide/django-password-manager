from django.urls import path, include

urlpatterns = [
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("", include("apps.passwords.urls", namespace="passwords"))
]
