from django.conf.urls import url
from notes.views import *	
from .ajax import delete_note

# We map our views with particular url with url namespce.
urlpatterns = [
    url(r'^$', NoteCreateView.as_view(), name='note-create'),
    url(r'^ajax/delete_note/$', delete_note, name='note-delete'),
]
