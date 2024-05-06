from django.contrib import admin
from ..models import *

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    ...

