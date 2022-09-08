from email import message
from django.shortcuts import render,redirect
from .models import User
from django.apps import apps
from django.contrib.auth import authenticate,login, logout
website_profile = apps.get_model('core', 'website_profile')
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
            return redirect('login')

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

    print(response.text)



    
def UserRegister(request):

    # if request.method == "POST":
    #     username = request.POST['name']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     password = request.POST['password']
    #     user = User.objects.create(username=username,email=email,phone_number=phone_number)
    #     user.set_password(password)
    #     user.save()
    #     messages.success(request, "Registration Successfull...")
    #     return redirect('login')
    #
    # else:
    #
    #
    #     data = website_profile.objects.all()
    #     return render(request, 'frontend/Register.html', {'result': data})

    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        check_user = User.objects.filter(email=email).first()
        check_profile = User.objects.filter(phone_number=phone_number).first()

        if check_user or check_profile:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'frontend/register.html', context)

        otp = str(random.randint(1000, 9999))
        user = User(username=username, email=email, phone_number=phone_number, otp=otp)
        user.set_password(password)

        user.save()

        # send_otp(phone_number, otp)
        # request.session['phone_number'] = phone_number
        return redirect('index')
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
            print('Wrong')

            context = {'message': 'Wrong OTP', 'class': 'danger', 'phone_number': phone_number}
            return render(request, 'otp.html', context)

    return render(request, 'main/otp.html', context)



