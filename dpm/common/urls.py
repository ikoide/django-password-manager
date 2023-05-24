from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("accounts/", include("apps.accounts.urls")),
    path("", include("apps.passwords.urls"))
]
