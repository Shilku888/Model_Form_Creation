from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from modelform.form import StudentRecordForm,StudentAddressForm

# Create your views here.
def modelform(request):
    if request.method == "POST":
        form_register = StudentRecordForm(request.POST)
        if form_register.is_valid():
            form_register.save()
        form_address = StudentAddressForm(request.POST)

    return render(request, 'modelform/modelform.html',
                  {"StudentRecordForm": StudentRecordForm,
                   "StudentAddressForm":StudentAddressForm,},
                  )
