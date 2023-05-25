from django.http import Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.passwords.models import Entry
from apps.passwords.forms import EntryForm

class VaultView(LoginRequiredMixin, CreateView):
    template_name = "passwords/vault.html"
    form_class = EntryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["entries"] = user.entries.all()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(VaultView, self).form_valid(form)

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("passwords:vault")

    def get_object(self, queryset=None):
        obj = super(EntryDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404

        return obj
