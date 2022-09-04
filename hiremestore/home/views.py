# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.apps import apps
from django.shortcuts import render, redirect
from core.models import *
from .form import *
from django.contrib import messages
from accounts.models import *
category = apps.get_model('core', 'Category')
subcategory = apps.get_model('core', 'SubCategory')

# @login_required(login_url="/login/")


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def Categorydisplay(request):
    data = category.objects.all()
    print('Category data', data)
    return render(request, 'home/category.html', {'categoryresult': data})


def Subategorydisplay(request):
    data = subcategory.objects.all()
    return render(request, 'home/subcategory.html', {'subcategoryresult': data})

# Category Crud Operation Start Here......................................................


def CategoryAdd(request):
    return render(request, 'home/category_add.html')


def CategorySave(request):
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        image = request.FILES['image']
        type = request.POST['type']
        category_done = Category.objects.create(
            name=name, title=title, image=image, type=type)
        category_done.save()
        return redirect('categorydisplay')

    else:
        return redirect('category_add')


def CategoryEdit(request, id):
    data = Category.objects.get(id=id)
    print(data)
    return render(request, 'home/category_add.html', {'category': data})


def CategoryUpdate(request, id):
    category_done = Category.objects.get(id=id)
    if request.POST['name']:
        category_done.name = request.POST['name']
    if request.POST['title']:
        category_done.title = request.POST['title']
    if request.FILES['image']:
        category_done.image = request.FILES['image']

    category_done.save()
    return redirect('categorydisplay')


def Category_Delete(request, id):
    data = Category.objects.get(id=id)
    data.delete()
    return redirect('categorydisplay')

# Category Crud Operation End Here......................................................

# Subcategory Crud Operation Start Here......................................................


def SubCategoryAdd(request):
    category = Category.objects.all().order_by('-created')
    content = {'category': category}
    category_dropdown = Category.objects.all().order_by('-created')[:4]
    content = {'category_dropdown': category_dropdown}
    return render(request, 'home/subcategory_add.html', content)


def SubCategorySave(request):
    if request.method == "POST":
        name = request.POST['name']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        description = request.POST['description']
        image = request.FILES['image']
        category_done = SubCategory.objects.create(
            name=name, description=description, image=image, cat=category)
        category_done.save()
        return redirect('subcategorydisplay')

    else:
        return redirect('subcategory_add')


def SubCategoryEdit(request, id):
    data = SubCategory.objects.get(id=id)
    category = Category.objects.filter(name=data.cat)
    category_dropdown = Category.objects.all().order_by('-created')[:4]
    return render(request, 'home/subcategory_add.html', {'subcategory': data, 'category': category, 'category_dropdown': category_dropdown})


def SubCategoryUpdate(request, id):
    subcategory_done = SubCategory.objects.get(id=id)
    if request.POST['category']:
        cat_id = request.POST['category']
        print(cat_id)
        category = Category.objects.get(id=cat_id)
        subcategory_done.cat = category
    if request.POST['name']:
        subcategory_done.name = request.POST['name']
    if request.POST['description']:
        subcategory_done.description = request.POST['description']
    # if request.FILES['image']:
    #     subcategory_done.image = request.FILES['image']

    subcategory_done.save()
    return redirect('subcategorydisplay')


def SubCategory_Delete(request, id):
    data = SubCategory.objects.get(id=id)
    data.delete()
    return redirect('subcategorydisplay')

# subCategory Crud Operation End Here......................................................


def AddCat(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('categorydisplay')
        else:
            messages.info(request, 'fill valid data')
            print('Data Not Upload')
    form = CategoryForm()
    context = {'form': form}

    return render(request, 'home/addcat.html', context)


def category_update(request, id):

    data = Category.objects.get(id=id)
    print(data)
    if request.method == 'POST':

        form = CategoryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('categorydisplay')

    else:
        form = CategoryForm(instance=data)
    return render(request, 'home/addcat.html', {'form': form})

# User Crud Operation Start Here......................................................

def UserDisplay(request):
    data = User.objects.all()
    return render(request, 'home/user.html', {'userresult': data})


def User_Detail_Data(request, id):
    # data = User.objects.get(id=id)
    # if User_Detail.objects.filter(user_id=data).exists():
    #     detail_data = User_Detail.objects.get(user_id=data)
    #     print('detatils', detail_data)
    #     return render(request, 'home/user_profile.html', {'user_detail_result': detail_data, 'userdata': data})
    # else:
    #     return redirect('userdisplay')
    pass


def User_Delete(request, id):
    data = User.objects.get(id=id)
    print(User.is_active)
    data.update()
    return redirect('userdisplay')


def contact_list(request):
    data = Contact.objects.all().order_by('-created')
    return render(request, 'home/user.html', {'contact_list': data})

# User Crud Operation End Here......................................................

# Website Profile Crud Operation Start Here......................................................

def Website_view(request):
    data = website_profile.objects.all()
    return render(request, 'home/website_profile.html', {'result': data})

def WebprofileAdd(request):
    return render(request, 'home/website_profile_add.html')


def Webprofilesave(request):
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        website_title = request.POST['title']
        website_subtitle = request.POST['subtitle']
        logo = request.FILES['logo']
        background_img = request.FILES['background_img']
        favicon = request.FILES['favicon']
        trusted_by = request.FILES.getlist("trusted_by")

        # fb_link = request.POST['fb_link']
        # instagram_link = request.POST['instagram_link']
        # twitter_link = request.POST['twitter_link']  

        fb_link = 'hdgh'
        instagram_link = 'ghgfhgh'
        twitter_link = 'ggfhg'

        web_profile_save = website_profile.objects.create(mobile_number=mobile_number,
        website_title=website_title,website_subtitle=website_subtitle,logo=logo,
        background_img=background_img,favicon=favicon,trusted_by=trusted_by,fb_link=fb_link,
        instagram_link=instagram_link,twitter_link=twitter_link)
        web_profile_save.save()

        return redirect('website_view')

    else:
        return redirect('webprofile_add')

def WebProfileEdit(request, id):
    data = website_profile.objects.get(id=id)
    return render(request, 'home/website_profile_add.html', {'webprofile': data})


def WebprofileUpdate(request, id):
    webprofile_done = website_profile.objects.get(id=id)
    if request.POST['title']:
        webprofile_done.website_title = request.POST['title']
    if request.POST['subtitle']:
        webprofile_done.website_subtitle = request.POST['subtitle']
    # if request.FILES['image']:
    #     subcategory_done.image = request.FILES['image']

    webprofile_done.save()
    return redirect('website_view')



# Website Profile Crud Operation End Here......................................................
