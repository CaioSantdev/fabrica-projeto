from django.contrib import admin
from ..models import *

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    ...
    