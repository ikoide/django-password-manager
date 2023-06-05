from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from encrypted_fields.fields import EncryptedTextField

from apps.accounts.models import Folder

User = get_user_model()

class Entry(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    username = models.CharField(max_length=48)
    password = EncryptedTextField()
    uri = models.CharField(max_length=128)
    notes = models.TextField()

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="entries")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")

    def get_absolute_url(self):
        return reverse("passwords:vault", kwargs={"pk": self.pk})
