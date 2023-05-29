from django import forms
from django.forms import Textarea

from apps.passwords.models import Entry
from apps.accounts.models import Folder

class EntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EntryForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["notes"].initial = self.instance.notes

        self.fields["folder"].queryset = self.user.folders.all()

    class Meta:
        model = Entry
        fields = ("name", "username", "password", "uri", "notes", "folder")
