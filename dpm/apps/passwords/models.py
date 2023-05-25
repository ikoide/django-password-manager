from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Entry(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    username = models.CharField(max_length=48)
    password = models.CharField(max_length=128)
    uri = models.CharField(max_length=128)
    notes = models.TextField()

    folder = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
