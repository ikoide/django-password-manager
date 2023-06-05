from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, FormView, TemplateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.accounts.mixins import UserIsOwnerMixin
from common.mixins import InvalidGetMixin
from apps.passwords.models import Entry
from apps.accounts.models import Folder
from apps.passwords.forms import EntryForm

class EntryView(LoginRequiredMixin, TemplateView):
    template_name = "passwords/vault.html"
    success_url = "passwords:vault"

    def get(self, request, *args, **kwargs):
        folder_name = request.GET.get("folder")
        search = request.GET.get("search")

        if folder_name:
            try:
                folder = Folder.objects.get(name=folder_name, user=request.user)
                self.entries = request.user.entries.filter(folder=folder)
            except Folder.DoesNotExist:
                messages.warning(request, f"Folder '{folder_name}' does not exist.")
                return redirect(self.success_url)

        elif search:
            self.entries = request.user.entries.filter(
                Q(name__icontains=search) |
                Q(username__icontains=search) |
                Q(uri__icontains=search)
            )

        else:
            self.entries = request.user.entries.all()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["entries"] = self.entries
        context["form"] = EntryForm(user=self.request.user)

        return context

class EntryCreateView(InvalidGetMixin, LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("passwords:vault")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(EntryCreateView, self).form_valid(form)

class EntryUpdateView(InvalidGetMixin, UserIsOwnerMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("passwords:vault")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

class EntryDeleteView(InvalidGetMixin, UserIsOwnerMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("passwords:vault")

class FolderCreateView(InvalidGetMixin, LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        folder_name = request.POST.get("name")
        if folder_name:
            Folder.objects.create(name=folder_name, user=request.user)

        return HttpResponseRedirect(reverse_lazy("passwords:vault"))
