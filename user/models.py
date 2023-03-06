from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.username
