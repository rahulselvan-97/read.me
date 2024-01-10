from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.
def login_view(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is None:
            context={'error':'invalid username or password'}
            return render(request,'login.html',context)
        login(request,user)
    return render(request,'login.html',{})

def logout_view(request):
    return render(request,'logout.html',{})

def register_view(request):
    return render(request,'register.html',{})