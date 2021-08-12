from django.contrib import admin
from modelform.models import StudentRecord,StudentAddress,ClassRecord,CollegeRecord


# Register your models here.
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'year', 'register_date')
    search_fields = ('name', 'register_date')

class StudentAddressAdmin(admin.ModelAdmin):
    list_display = ('city','pin')
    search_fields = ('city', 'pin')

admin.site.register(StudentRecord, StudentRecordAdmin)
admin.site.register(StudentAddress, StudentAddressAdmin)

class ClassRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'register_date')
    search_fields = ('name', 'register_date')


admin.site.register(ClassRecord, ClassRecordAdmin)

class CollegeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'register_date')
    search_fields = ('name', 'register_date')


admin.site.register(CollegeRecord, CollegeRecordAdmin)

