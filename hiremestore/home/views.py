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
from django.shortcuts import render
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

def category_form(request):
    # data= subcategory.objects.all()
    return render(request, 'home/category_form.html', )