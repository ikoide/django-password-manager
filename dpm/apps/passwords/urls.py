from django.urls import path
from apps.passwords import views

app_name = "passwords"

urlpatterns = [
    path("", views.VaultView.as_view(), name="vault"),
    path("entries/<int:pk>/delete/", views.EntryDeleteView.as_view(), name="delete"),
]
