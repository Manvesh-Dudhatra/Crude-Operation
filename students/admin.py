from django.contrib import admin
from students.models import Student

class studentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'std')

admin.site.register(Student, studentAdmin)
