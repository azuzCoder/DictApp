from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=255)


class Word(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    folder = models.ForeignKey(to=Folder, on_delete=models.CASCADE, related_name='word')
