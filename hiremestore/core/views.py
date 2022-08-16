
from .models import *
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


def base(request):
    data = website_profile.objects.all()


    print(data)
    return render(request, 'main/index.html', {'result': data})


