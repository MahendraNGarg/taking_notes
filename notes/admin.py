# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Note

# Register your models here.

# Register Note model in admin to manage notes from admin.
admin.site.register(Note)