from snippets.models import Department, Doctor, Snippet
from django.contrib import admin

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')


admin.site.register(Snippet)
admin.site.register(Department)
admin.site.register(Doctor, DoctorAdmin)
