from .models import *
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User
from django.core import serializers
from django.http import HttpResponse
from .filters import CategoryFilter

def Global_Data(request):
    city = Cities.objects.filter()[:4]
    category = Category.objects.filter().order_by('-created')[:8]
    return {'headcity': city, 'headcategory':category}

def index(request):
    digital = Category.objects.filter(type=1).order_by('-created')[:8]
    helper = Category.objects.filter(type=2).order_by('-created')[:4]
    category = Category.objects.filter().order_by('-created')[:8]
    subcategory = SubCategory.objects.filter().order_by('-created')
    data = website_profile.objects.all()
    testimonial = Testimonails.objects.all()
    user = User_Detail.objects.all()
    category_Filter = CategoryFilter(request.GET,queryset=user)
    
    content = {'result': data, 'testimonial': testimonial, 'category': category,
               'subcategory': subcategory, 'digital': digital, 'helper': helper,'category_filter': category_Filter}
    return render(request, 'frontend/index.html', content)


def SearchCategory(request):
    user = User_Detail.objects.all()
    category_Filter = CategoryFilter(request.GET,queryset=user)
    print(request.GET)
    return render(request, 'frontend/searchcategory.html', {'category_filter': category_Filter})

def Browsebylocation(request):
    city = Cities.objects.all()[:8]
    return render(request, 'frontend/browse-jobs-location.html', {'city': city})


def Browsebyskill(request):
    digital = Category.objects.filter(type=1).order_by('-created')[:8]
    return render(request, 'frontend/browse-jobs-skill.html', {'digital': digital})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mobile = request.POST['mobile']
        message = request.POST['message']

        contact = Contact.objects.create(
            name=name, email=email, subject=subject, mobile=mobile, message=message,)
        contact.save()

        messages.info('Message is send')
        return redirect('contact')

    data = website_profile.objects.all()
    return render(request, 'main/contact.html', {'result': data},)


def about(request):
    data = website_profile.objects.all()
    return render(request, 'main/about.html', {'result': data}, )


def servies(request):
    data = website_profile.objects.all()
    Category_data = Category.objects.filter().order_by('-created')
    return render(request, 'main/category.html', {'category': Category_data, 'result': data})


def subcategory(request, id):
    data = website_profile.objects.all()
    Category_data = Category.objects.filter(slug=id)
    cat = Category.objects.filter(slug=id).values_list('id', flat=True)
    cate = list(cat)
    get = cate[0]
    subcategory = SubCategory.objects.filter(
        cat_id=get).order_by('-created')[:10]
    context = {'subcategory': subcategory,
               'result': data, 'Category_data': Category_data, }
    return render(request, 'frontend/sub-category.html', context)


def worker(request, id):
    data = website_profile.objects.all()
    subcategory = SubCategory.objects.filter(
        slug=id).values_list('id', flat=True)
    print(subcategory)
    cate = list(subcategory)
    get = cate[0]
    worker = User_Detail.objects.filter(sub_category=get)
    return render(request, 'frontend/helper.html', {'result': data, 'worker': worker}, )


def worker_detail(request, id):
    data = website_profile.objects.all()
    worker = User_Detail.objects.filter(slug=id).first()
    return render(request, 'frontend/helper-detail.html', {'result': data, 'worker': worker, }, )


def update_profile(request, id):
    user = User_Detail.objects.filter(slug=id).first()
    country = Country.objects.filter(id=101)
    city = Cities.objects.all()
    state = States.objects.all()
    return render(request, 'frontend/myprofile.html', {'worker': user, 'country': country, 'city': city, 'state': state})


def update_profile_update(request, id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        worker_data = User_Detail.objects.filter(user=user).first()
        if worker_data:
            worker_data = worker_data
        else:
            worker_data = User_Detail()
            worker_data.user = user
        category = Category.objects.filter(request.POST['category'])
        worker_data.category =category
        subcategory = SubCategory.objects.filter(request.POST['subcategory'])
        worker_data.sub_category = subcategory
        worker_data.name = request.POST['name']
        worker_data.email = request.POST['email']
        worker_data.dob = request.POST['dob']
        worker_data.area = request.POST['area']
        worker_data.city = request.POST['city']
        worker_data.district = request.POST['district']
        worker_data.zip = request.POST['zip']
        worker_data.state = request.POST['state']
        worker_data.country = request.POST['country']
        worker_data.mobile = request.POST['mobile']
        worker_data.charges = request.POST['rate']
        worker_data.experiance = request.POST['exp']
        worker_data.bio = request.POST['bio']
        worker_data.discription = request.POST['desc']
        if request.FILES.get('image'):
            worker_data.image = request.FILES.get('image')

        worker_data.save()

        messages.success(request, 'Data Updated...')
        return redirect('index')

    else:
        return redirect('update_profile')


def Helper_DashBoard(request):
    data = User_Detail.objects.filter(slug='saurabh-soni').first()
    return render(request, 'frontend/helper-dashboard.html', {'helper': data})


def GetCategory(request):
    data = Category.objects.filter(type=1)
    jsondata = serializers.serialize('json', data)
    return HttpResponse(jsondata, content_type='application/json')


def GetSubCategory(request):
    data = User_Detail.objects.filter(slug='saurabh-soni').first()
    return render(request, 'frontend/helper-dashboard.html', {'helper': data})
