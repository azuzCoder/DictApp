from django import forms

from .models import Folder, Word


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ['name']


class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['word', 'translation', 'description', 'folder']
