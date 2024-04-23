from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    ...

class CourseAdmin(admin.ModelAdmin):
    ...

class CampunsAdmin(admin.ModelAdmin):
    ...

admin.site.register(Student,StudentAdmin)
admin.site.register(Courses,CourseAdmin)
admin.site.register(Campus,CampunsAdmin)