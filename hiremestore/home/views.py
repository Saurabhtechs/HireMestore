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
from django.shortcuts import render,redirect
from core.models import *
from .form import *
from django.contrib import messages
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
    data= category.objects.all()
    print('Category data',data)
    return render(request, 'home/category.html', {'categoryresult': data} )

def Subategorydisplay(request):
    data= subcategory.objects.all()
    return render(request, 'home/subcategory.html', {'subcategoryresult': data})

# Category Crud Operation Start Here......................................................
def CategoryAdd(request):
    return render(request,'home/category_add.html')

def CategorySave(request):
    if request.method=="POST":
        name = request.POST['name']
        title = request.POST['title']
        image = request.FILES['image']
        category_done = Category.objects.create(name=name,title=title,image=image)
        category_done.save()
        return redirect('categorydisplay')

    else:
        return redirect('category_add')

def CategoryEdit(request,id):
    data = Category.objects.get(id=id)
    print(data)
    return render(request,'home/category_add.html',{'category':data})

def CategoryUpdate(request,id):
    category_done = Category.objects.get(id=id)
    if request.POST['name']:    
        category_done.name = request.POST['name']
    if request.POST['title']:
        category_done.title = request.POST['title']
    if request.FILES['image']:
        category_done.image = request.FILES['image']
        
    category_done.save()
    return redirect('categorydisplay')

def Category_Delete(request,id):
    data = Category.objects.get(id=id)
    data.delete()
    return redirect('categorydisplay')

# Category Crud Operation End Here......................................................

# Subcategory Crud Operation Start Here......................................................

def SubCategoryAdd(request):
    category = Category.objects.all().order_by('-created')[:4]
    content = {'category': category}
    return render(request,'home/subcategory_add.html',content)

def SubCategorySave(request):
    if request.method=="POST":
        name = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        image = request.FILES['image']
        category_done = SubCategory.objects.create(cat=category,name=name,description=description,image=image)
        category_done.save()
        return redirect('subcategorydisplay')

    else:
        return redirect('subcategory_add')

def SubCategoryEdit(request,id):
    data = SubCategory.objects.get(id=id)
    print(data)
    return render(request,'home/subcategory_add.html',{'subcategory':data})

def SubCategoryUpdate(request,id):
    subcategory_done = SubCategory.objects.get(id=id)
    if request.POST['category']:    
        subcategory_done.name = request.POST['category']
    if request.POST['name']:    
        subcategory_done.name = request.POST['name']
    if request.POST['description']:
        subcategory_done.description = request.POST['description']
    if request.FILES['image']:
        subcategory_done.image = request.FILES['image']
        
    subcategory_done.save()
    return redirect('subcategorydisplay')

def SubCategory_Delete(request,id):
    data = SubCategory.objects.get(id=id)
    data.delete()
    return redirect('subcategorydisplay')

# Category Crud Operation End Here......................................................

def AddCat(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES )
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