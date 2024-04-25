from django.contrib import admin
from .models import *
# Register your models here.

class EstudanteAdmin(admin.ModelAdmin):
    readonly_fields = ['matriculaEstudante']

class CursosAdmin(admin.ModelAdmin):
    ...

class CampusAdmin(admin.ModelAdmin):
    ...

admin.site.register(Estudante,EstudanteAdmin)
admin.site.register(Cursos,CursosAdmin)
admin.site.register(Campus,CampusAdmin)