from email import message
from django.shortcuts import render,redirect
from .models import User
from django.apps import apps
from django.contrib.auth import authenticate,login, logout
website_profile = apps.get_model('core', 'website_profile')
from django.contrib import messages
# Create your views here.


def AdminLogin(request):
    # data = website_profile.objects.all()
    return render(request, 'home/login.html')

def Login(request):
    data = website_profile.objects.all()
    return render(request, 'main/login.html', {'result': data})

def AdminLogincheck(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = authenticate(phone_number=phone_number, password=password)
            
        if user:
            # if user.is_active:
            login(request, user)
            return redirect('/admin')
        else:
            return redirect('login')


def Logincheck(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = authenticate(phone_number=phone_number, password=password)
            
        if user:
            # if user.is_active:
            login(request, user)
            messages.success(request,"Login Successfull...")
            return redirect('/')
        else:
            return redirect('login')

def Logout(request):
    logout(request)
    messages.success(request,"Logout Successfull...")
    return redirect('index')

def Register(request):
    data = website_profile.objects.all()
    return render(request,'main/Register.html',{'result':data})

def UserRegister(request):

    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = User.objects.create(username=username,email=email,phone_number=phone_number)
        user.set_password(password)
        user.save()
        messages.success(request, "Registration Successfull...")
        return redirect('login')

    else:


        data = website_profile.objects.all()
        return render(request, 'main/Register.html', {'result': data})

