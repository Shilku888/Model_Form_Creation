from django import  forms
from  modelform.models import StudentRecord

class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = ('name','age','year')