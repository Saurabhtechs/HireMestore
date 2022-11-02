from email import message
from django.shortcuts import render,redirect
from .models import User
from django.apps import apps
from django.contrib.auth import authenticate,login, logout
website_profile = apps.get_model('core', 'website_profile','User_Detail')
from  core.models import *


from django.contrib import messages

import random
import http.client

from django.conf import settings
from django.contrib.auth import authenticate, login

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
            return redirect('index')
        else:
            msg = messages.success(request, "something wrong")
            return msg

def Logout(request):
    logout(request)
    messages.success(request,"Logout Successfull...")
    return redirect('index')

def Register(request):
    data = website_profile.objects.all()
    return render(request,'frontend/register.html',{'result':data})




# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# def send_otp(phone_number , otp):
#     print("FUNCTION CALLED")
#     conn = http.client.HTTPSConnection("api.msg91.com")
#     authkey = settings.AUTH_KEY
#     headers = { 'content-type': "application/json" }
#     url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&phone_number="+phone_number+"&authkey="+authkey+"&country=91"
#     conn.request("GET", url , headers=headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data)
#     return None

def send_otp(phone_number , otp):
    # print("FUNCTION CALLED")
    # conn = http.client.HTTPSConnection("api.msg91.com")
    # authkey = settings.AUTH_KEY
    # headers = { 'content-type': "application/json" }
    # url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&phone_number="+phone_number+"&authkey="+authkey+"&country=91"
    # conn.request("GET", url , headers=headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data)
    # return None

    import requests

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=FSTSMS&message=GoodMorning&language=english&route=p&numbers=7879543263,"
    headers = {
        'authorization': "dDeBKh1N48tT0yE2MYGcrWIoJ39jaAUQFOHzbpisVmuxkCvwqf7Hp3QTKvtXVEb56fMcuOPjAn8W1FDs",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)




    
def UserRegister(request):

    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        # otp = request.POST['otp']
        # print(otp)
        # if otp != '123456':
        #     messages.info(request, 'otp is invalid')
        #     return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'email Taken')
            return redirect('register')

        if User.objects.filter(phone_number=phone_number).exists():
            messages.info(request, 'Mobile number Taken')
            return redirect('register')

        user = User(username=username, email=email, phone_number=phone_number)
        user.set_password(password)

        user.save()

        worker_data = User_Detail()
        worker_data.name = request.POST['name']
        worker_data.email = request.POST['email']
        worker_data.phone = request.POST['phone_number']
        worker_data.user_id = user.id
        worker_data.save()
        messages.success(request,'Registerd Successfully')
        # send_otp(phone_number, otp)
        # request.session['phone_number'] = phone_number
        # return redirect('index')
    return render(request, 'frontend/register.html')


def otp(request):
    phone_number = request.session['phone_number']
    context = {'phone_number': phone_number}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = User.objects.filter(phone_number=phone_number).first()

        if otp == profile.otp:
            return redirect('index')
        else:
            context = {'message': 'Wrong OTP', 'class': 'danger', 'phone_number': phone_number}
            return render(request, 'otp.html', context)

    return render(request, 'main/otp.html', context)



