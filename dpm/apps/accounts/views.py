from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from apps.accounts.models import User
from apps.accounts.forms import RegistrationForm

class RegistrationView(CreateView):
    template_name = "registration/register.html"
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context["next"] = self.request.GET.get("next")

        return context

    def get_success_url(self):
        next_url = self.request.POST.get("next")
        success_url = reverse("accounts:login")
        if next_url:
            success_url += "?next={}" % next_url

        return success_url

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("accounts:login")
    
    def get_object(self, queryset=None):
        user = self.request.user

        return user 
