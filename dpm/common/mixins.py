from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class InvalidGetMixin:
    def get(self, request, *args, **kwargs):
        messages.add_message(request, messages.ERROR, "Invalid request method.")
        return HttpResponseRedirect(reverse_lazy("passwords:vault"))
