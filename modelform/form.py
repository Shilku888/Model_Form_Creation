from django import  forms
from  modelform.models import StudentRecord,StudentAddress

class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = ('name','age','year')

class StudentAddressForm(forms.ModelForm):
    class Meta:
        model = StudentAddress
        fields =('city','pin')