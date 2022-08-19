
from .models import *
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):

    category = Category.objects.filter().order_by('-created')[:4]
    subcategory = SubCategory.objects.filter().order_by('-created')[:9]
    data = website_profile.objects.all()
    testimonial = Testimonails.objects.all()
    content = {'result': data, 'testimonial': testimonial, 'category': category, 'subcategory': subcategory,}
    return render(request, 'main/index.html', content)


def contact(request):
    data = website_profile.objects.all()
    return render(request, 'main/contact.html', {'result': data},)


def about(request):
    data = website_profile.objects.all()
    return render(request, 'main/about.html', {'result': data}, )

def servies(request):
    data = website_profile.objects.all()
    return render(request, 'main/servies.html', {'result': data}, )


