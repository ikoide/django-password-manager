from django.views import View
from django.shortcuts import render

from apps.passwords.models import Entry

class VaultView(View):
    def get(self, request):
        entries = Entry.objects.all()
        return render(request=request, template_name="passwords/vault.html", context={"entries": entries})
