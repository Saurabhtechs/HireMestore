from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
# Create your views here.

def Index(request):
    return render(request,'index.html')


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