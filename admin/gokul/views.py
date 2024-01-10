from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from.forms import employee_date
from.models import Employee,articles
from .forms import NameForm
# Create your views here.

def stunners(request):
   articles_object=articles.objects.all()
   title=request.POST.get('title')
   print(title)
   
   context={'articles':articles_object}
   if request.method=="POST":
        form=employee_date(request.POST)
        if form.is_valid():
            name=form.cleaned_data['emp_name']
            salary=form.cleaned_data['emp_salary']
            emp=Employee.objects.create(emp_name=name,emp_salary=salary)
            emp.save()
            return HttpResponse('data has been saved')
            
   form=employee_date ()    
   return render(request,'person.html',{'form':form,'context':context})

def article_search_view(request):
    context={}
    return render(request,'search.html',context=context)


def get_name(request):
    obj=Employee.objects.get(id=4)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
