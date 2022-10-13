from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
