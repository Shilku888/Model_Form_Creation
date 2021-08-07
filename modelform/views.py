from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from modelform.form import StudentRecordForm

# Create your views here.
def modelform(request):
    if request.method == "POST":
        form_register = StudentRecordForm(request.POST)
        if form_register.is_valid():
            form_register.save()

    return render(request, 'modelform/modelform.html',
                  {"StudentRecordForm": StudentRecordForm,},
                  )