from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from.forms import employeeform
from.models import employee
# Create your views here.
def employeedata(request):
    if request.method=="POST":
       form =employeeform(request.POST)
       if form.is_valid():
           name=form.cleaned_data['emp_name']
           salary=form.cleaned_data['emp_salary']
           emp=employee.objects.create(emp_name=name,emp_salary=salary)
           emp.save()
           return HttpResponse('data saved in data base')
    form=employeeform()
    return render(request,'emp.html',{'form':form})




def current_datetime(request):
    now = datetime.datetime.now()
    users=['rahul','gokul']
    
    return render(request,'index.html',{'now':now,'us':users})



