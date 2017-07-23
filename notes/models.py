# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import reverse

# create a note model with it's charecterisitc fields like title, description, and created, in created we pass a default date when a new note created it will add created time default.
class Note(models.Model):
    """
    Description: Created a model to store Notes fields like title, description and created.
    """
    
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('note-create')

    def __str__(self):   
        return self.title