from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.accounts.managers import BaseUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_online = models.DateTimeField(null=True)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

class Folder(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")

    def __str__(self):
        return f"{self.name}"

@receiver(post_save, sender=User)
def create_folder(sender, instance, created, **kwargs):
    if created:
        Folder.objects.create(name="No Folder", user=instance)
