# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from accounts.models import *
from core.models import *
from django import template
from django.apps import apps
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from .form import *


def AdminLogin(request):
    return render(request, 'home/login.html')


def AdminLogincheck(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = authenticate(phone_number=phone_number, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('admin')


@login_required(login_url="/admin/")
def index(request):
    category = Category.objects.count()
    subcategory = SubCategory.objects.count()
    total_Worker = User_Detail.objects.count()
    context = {'segment': 'index',
               'category': category,
               'subcategory': subcategory,
               'total_Worker': total_Worker}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/admin/")
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

@login_required(login_url="/admin/")
def Categorydisplay(request):
    data = Category.objects.all()
    return render(request, 'home/category.html', {'categoryresult': data})


@login_required(login_url="/admin/")
def Subategorydisplay(request):
    data = SubCategory.objects.all()
    return render(request, 'home/subcategory.html', {'subcategoryresult': data})

# Category Crud Operation Start Here......................................................


@login_required(login_url="/admin/")
def CategoryAdd(request):
    return render(request, 'home/category_add.html')


@login_required(login_url="/admin/")
def CategorySave(request):
    try:
        if request.method == "POST":
            name = request.POST['name']
            title = request.POST['title']
            image = request.FILES.get('image')
            type = request.POST['type']
            category_done = Category.objects.create(
                name=name, title=title, image=image, type=type)
            category_done.save()
            return redirect('categorydisplay')
    except Exception as e:
        messages.info(request, e)
        return render(request, 'home/category_add.html')


@login_required(login_url="/admin/")
def CategoryEdit(request, id):
    data = Category.objects.get(id=id)
    return render(request, 'home/category_add.html', {'category': data})


@login_required(login_url="/admin/")
def CategoryUpdate(request, id):
    category_done = Category.objects.get(id=id)
    if request.POST['type']:
        category_done.type = request.POST['type']
    if request.POST['name']:
        category_done.name = request.POST['name']
    if request.POST['title']:
        category_done.title = request.POST['title']
    if request.FILES.get('image'):
        category_done.image = request.FILES.get('image')

    category_done.save()
    return redirect('categorydisplay')


@login_required(login_url="/admin/")
def Category_Delete(request, id):
    data = Category.objects.get(id=id)
    data.delete()
    return redirect('categorydisplay')

# Category Crud Operation End Here......................................................

# Subcategory Crud Operation Start Here......................................................


@login_required(login_url="/admin/")
def SubCategoryAdd(request):
    category = Category.objects.all().order_by('-created')
    content = {'category': category}
    category_dropdown = Category.objects.all().order_by('-created')
    content = {'category_dropdown': category_dropdown}
    return render(request, 'home/subcategory_add.html', content)


@login_required(login_url="/admin/")
def SubCategorySave(request):
    if request.method == "POST":
        name = request.POST['name']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        description = request.POST['description']
        image = request.FILES.get('image')
        category_done = SubCategory.objects.create(
            name=name, description=description, image=image, cat=category)
        category_done.save()
        return redirect('subcategorydisplay')

    else:
        return redirect('subcategory_add')


@login_required(login_url="/admin/")
def SubCategoryEdit(request, id):
    data = SubCategory.objects.get(id=id)
    category = Category.objects.filter(name=data.cat)
    category_dropdown = Category.objects.all().order_by('-created')
    return render(request, 'home/subcategory_add.html', {'subcategory': data, 'category': category, 'category_dropdown': category_dropdown})


@login_required(login_url="/admin/")
def SubCategoryUpdate(request, id):
    subcategory_done = SubCategory.objects.get(id=id)
    if request.POST['category']:
        cat_id = request.POST['category']
        category = Category.objects.get(id=cat_id)
        subcategory_done.cat = category
    if request.POST['name']:
        subcategory_done.name = request.POST['name']
    if request.POST['description']:
        subcategory_done.description = request.POST['description']
    if request.FILES.get('image'):
        subcategory_done.image = request.FILES.get('image')

    subcategory_done.save()
    return redirect('subcategorydisplay')


@login_required(login_url="/admin/")
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
    form = CategoryForm()
    context = {'form': form}

    return render(request, 'home/addcat.html', context)


@login_required(login_url="/admin/")
def category_update(request, id):

    data = Category.objects.get(id=id)
    if request.method == 'POST':

        form = CategoryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('categorydisplay')

    else:
        form = CategoryForm(instance=data)
    return render(request, 'home/addcat.html', {'form': form})

# User Crud Operation Start Here......................................................


@login_required(login_url="/admin/")
def UserDisplay(request):
    data = User.objects.all()
    return render(request, 'home/user.html', {'userresult': data})


@login_required(login_url="/admin/")
def User_Detail_Data(request, id):
    # data = User.objects.get(id=id)
    # if User_Detail.objects.filter(user_id=data).exists():
    #     detail_data = User_Detail.objects.get(user_id=data)
    #     return render(request, 'home/user_profile.html', {'user_detail_result': detail_data, 'userdata': data})
    # else:
    #     return redirect('userdisplay')
    pass


@login_required(login_url="/admin/")
def User_Delete(request, id):
    data = User.objects.get(id=id)
    data.update()
    return redirect('userdisplay')


@login_required(login_url="/admin/")
def contact_list(request):
    data = Contact.objects.all()
    return render(request, 'home/contactdetail.html', {'contact_list': data})


@login_required(login_url="/admin/")
def contact_listdelete(request, id):
    data = Contact.objects.get(id=id)
    data.delete()
    return redirect('contact_list')

# User Crud Operation End Here......................................................

# Website Profile Crud Operation Start Here......................................................


@login_required(login_url="/admin/")
def Website_view(request):
    data = website_profile.objects.all()
    return render(request, 'home/website_profile.html', {'result': data})


@login_required(login_url="/admin/")
def WebprofileAdd(request):
    return render(request, 'home/website_profile_add.html')


@login_required(login_url="/admin/")
def Webprofilesave(request):
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        website_title = request.POST['title']
        website_subtitle = request.POST['subtitle']
        logo = request.FILES.get('logo')
        background_img = request.FILES.get('background_img')
        favicon = request.FILES.get('favicon')
        # trusted_by = request.FILES.getlist("trusted_by")

        # fb_link = request.POST['fb_link']
        # instagram_link = request.POST['instagram_link']
        # twitter_link = request.POST['twitter_link']

        fb_link = 'hdgh'
        instagram_link = 'ghgfhgh'
        twitter_link = 'ggfhg'
        for file in request.FILES.getlist("trusted_by"):
            web_profile_save = website_profile.objects.create(mobile_number=mobile_number,
                                                              website_title=website_title, website_subtitle=website_subtitle, logo=logo,
                                                              background_img=background_img, favicon=favicon, trusted_by=file, fb_link=fb_link,
                                                              instagram_link=instagram_link, twitter_link=twitter_link)
        web_profile_save.save()

        return redirect('website_view')

    else:
        return redirect('webprofile_add')


@login_required(login_url="/admin/")
def WebProfileEdit(request, id):
    data = website_profile.objects.get(id=id)
    return render(request, 'home/website_profile_add.html', {'webprofile': data})


@login_required(login_url="/admin/")
def WebprofileUpdate(request, id):
    webprofile_done = website_profile.objects.get(id=id)
    if request.POST['title']:
        webprofile_done.website_title = request.POST['title']
    if request.POST['subtitle']:
        webprofile_done.website_subtitle = request.POST['subtitle']
    if request.FILES.get('logo'):
        webprofile_done.image = request.FILES.get('logo')
    if request.FILES.get('logo'):
        webprofile_done.image = request.FILES.get('logo')
    if request.FILES.get('logo'):
        webprofile_done.image = request.FILES.get('logo')
    if request.FILES.get('logo'):
        webprofile_done.image = request.FILES.get('logo')

    webprofile_done.save()
    return redirect('website_view')


# Website Profile Crud Operation End Here......................................................


# Subscriber Crud Operation Start Here......................................................

@login_required(login_url="/admin/")
def SubscriberDisplay(request):
    data = SubScribers.objects.all()
    return render(request, 'home/subscriber.html', {'sresult': data})


@login_required(login_url="/admin/")
def subscriber_listdelete(request, id):
    data = SubScribers.objects.get(id=id)
    data.delete()
    return redirect('subscriberdisplay')
# Subscriber Crud Operation End Here......................................................
