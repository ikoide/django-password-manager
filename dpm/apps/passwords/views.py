from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render

from apps.passwords.models import Entry
from apps.passwords.forms import EntryForm

class VaultView(CreateView):
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
