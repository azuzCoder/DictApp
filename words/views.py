from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Folder, Word
from .forms import FolderForm, WordForm


def get_folders():
    return Folder.objects.all()


def get_words(pk):
    return Word.objects.filter(folder_id=pk)


class FolderCreateListView(View, LoginRequiredMixin):

    def get(self, request):
        context = {
            'folders': get_folders()
        }
        return render(request, 'folder.html', context)

    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('words:folder-cl')


class FolderRetrieveUpdateView(View, LoginRequiredMixin):

    def get(self, request, pk):
        try:
            folder = Folder.objects.get(pk=pk)
        except:
            return redirect('users:home')
        context = {
            'folder_id': pk,
            'words': get_words(pk)
        }
        return render(request, 'word.html', context)

    def post(self, reqeuest):
        form = FolderForm(reqeuest.POST)
        if form.is_valid():
            form.save()
        return redirect('users:home')


class WordCreateView(View, LoginRequiredMixin):

    def post(self, request):
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("words:folder-ru", pk=request.POST['folder'])


class FolderDestroyView(View):

    def get(self, request, pk):
        folder = Folder.objects.get(pk=pk)
        folder.delete()
        return redirect('words:folder-cl')
