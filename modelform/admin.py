from django.contrib import admin
from modelform.models import StudentRecord


# Register your models here.
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'year', 'register_date')
    search_fields = ('name', 'register_date')


admin.site.register(StudentRecord, StudentRecordAdmin)
