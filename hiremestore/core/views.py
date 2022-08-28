
from traceback import print_tb
from .models import *
# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *
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
    if request.GET['category']:
        subcategory = SubCategory.objects.filter(id=request.GET['category']).order_by('-created')[:9]
    elif request.GET['category']=="":
        subcategory = SubCategory.objects.all().order_by('-created')[:9]
    data = website_profile.objects.all()
    return render(request, 'main/sub_category.html', {'result': data, 'subcategory': subcategory}, )


def Category_data(request):
    data = User.objects.all()
    return data
   
print(Category_data)