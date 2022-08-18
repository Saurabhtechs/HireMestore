from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib.auth import authenticate,login, logout
website_profile = apps.get_model('core', 'website_profile')

from rest_framework.decorators import api_view
# Create your views here.


def Login(request):
    # data = website_profile.objects.all()
    return render(request, 'home/login.html')

def Logincheck(request):
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

def Logout(request):
    return redirect('index')

# def UserRegistration(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User(username=username,email=email,password=password)
#         user.save()
#         user_role = UserRole()
#         user_role.mobile_number= request.POST['mobile_number']
#         # user_role.role = request.POST['role']
#         user_role.save()
#         return redirect('https://legalguruindia.com')
#     else:
#         return redirect('home')