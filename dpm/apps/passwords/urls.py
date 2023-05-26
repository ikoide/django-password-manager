from django.urls import path
from apps.passwords import views

app_name = "passwords"

urlpatterns = [
    path("", views.EntryView.as_view(), name="vault"),
    path("entries/new", views.EntryCreateView.as_view(), name="new"),
    path("entries/<int:pk>/edit", views.EntryUpdateView.as_view(), name="edit"),
    path("entries/<int:pk>/delete/", views.EntryDeleteView.as_view(), name="delete"),
]
