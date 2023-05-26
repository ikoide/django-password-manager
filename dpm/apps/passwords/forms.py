from django import forms

from apps.passwords.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("name", "username", "password", "uri", "notes")
