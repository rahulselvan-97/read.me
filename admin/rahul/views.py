from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,'your account has been succesfully created')
        return redirect(request,'signin')
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def signout(request):
    return render(request,'signout.html')