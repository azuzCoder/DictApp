from django.urls import path

from .views import FolderCreateListView, FolderRetrieveUpdateView, WordCreateView, FolderDestroyView


app_name = 'words'
urlpatterns = [
    path('folder/<int:pk>', FolderRetrieveUpdateView.as_view(), name='folder-ru'),
    path('folder', FolderCreateListView.as_view(), name='folder-cl'),
    path('folder/delete/<int:pk>', FolderDestroyView.as_view(), name='folder-d'),

    path('word', WordCreateView.as_view(), name='word-c'),
]