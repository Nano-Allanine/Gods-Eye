from django.contrib import admin
from .models import Student, Faculty


# inorder to create your own display of data
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "course", "faculty"]
    # we can filter 
    # we can search by any field
    search_fields = ['first_name', 'last_name']
    # WE NEED TO BE ABLE TO EDIT  items while not openinng each entry
    list_editable = ['course']
    # Displaying in order(ascending)
    ordering = ['id']


class FacultyDisplay(admin.ModelAdmin):
    list_display = ["faculty_name", "department"]


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty)
