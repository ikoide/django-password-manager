from django import forms
from django.forms import Textarea

from apps.passwords.models import Entry

class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["notes"].initial = self.instance.notes

    class Meta:
        model = Entry
        fields = ("name", "username", "password", "uri", "notes")
