# -*- coding: utf-8 -*-

from django.views.generic.edit import CreateView
from .models import Note
from datetime import datetime

# A Create Class base view that we used to create notes. 
class NoteCreateView(CreateView):
    
    model = Note
    template_name = 'index.html'
    fields = ['title', 'description']

    def get_context_data(self, **kwargs):
        context = super(NoteCreateView, self).get_context_data(**kwargs)
        notes = Note.objects.all().order_by('-id')
        context['notes'] = notes
        context['time'] = datetime.now()
        return context
