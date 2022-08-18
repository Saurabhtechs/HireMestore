
from .models import *
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Coreindex(request):
    data = website_profile.objects.all()
    testimonial = Testimonails.objects.all()
    return render(request, 'main/index.html', {'result': data, 'testimonial': testimonial, })


def contact(request):
    data = website_profile.objects.all()
    return render(request, 'main/contact.html', {'result': data},)


def about(request):
    data = website_profile.objects.all()
    return render(request, 'main/about.html', {'result': data}, )


# def Login(request):
#     if User.p