from django.db import models

class Entry(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48)
    username = models.CharField(max_length=48)
    password = models.CharField(max_length=128)
    uri = models.CharField(max_length=128)
    notes = models.TextField()

    ## TODO user, folder
