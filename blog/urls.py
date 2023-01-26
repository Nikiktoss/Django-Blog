from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main_page"),
    path('view', view_all_notes, name="view_notes"),
    path('share/email/<slug:slug>', share_email, name='share_email_page'),
    path('add', add_note, name='add_note_page'),
    path('search', search_for_note, name="search_page"),
    path('update/<slug:slug>', update_note, name='update_note_page'),
    path('delete/notes', delete_some_notes, name='delete_some_notes_page'),
    path('delete/<slug:slug>', delete_note, name='delete_note_page'),
    path('<slug:slug>', note_view, name="note_page"),
]
