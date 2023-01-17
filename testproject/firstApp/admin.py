from django.contrib import admin
from firstApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']


admin.site.register(Student,StudentAdmin)


# Register your models here.
