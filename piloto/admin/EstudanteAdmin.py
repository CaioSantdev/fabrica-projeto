from django.contrib import admin
from ..models import *
# Register your models here.
@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    readonly_fields = ['matricula',]
    