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


def index(request):
    digital = Category.objects.filter(type=1).order_by('-created')[:4]
    helper = Category.objects.filter(type=2).order_by('-created')[:4]
    category = Category.objects.filter().order_by('-created')
    subcategory = SubCategory.objects.filter().order_by('-created')
    data = website_profile.objects.all()
    testimonial = Testimonails.objects.all()
    content = {'result': data, 'testimonial': testimonial, 'category': category,
               'subcategory': subcategory, 'digital': digital, 'helper': helper, }
    return render(request, 'main/index.html', content)


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


# def servies(request):
#     if request.GET['category']:
#         subcategory = SubCategory.objects.filter(cat=request.GET['category']).order_by('-created')[:9]
#     elif request.GET['category']=="":
#         subcategory = SubCategory.objects.all().order_by('-created')[:9]
#     else:
#         subcategory = SubCategory.objects.all().order_by('-created')[:9]
#
#     data = website_profile.objects.all()
#     return render(request, 'main/sub_category.html', {'result': data, 'subcategory': subcategory}, )

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
    return render(request, 'main/sub_category.html', context)


def worker(request, id):
    data = website_profile.objects.all()
    worker = User_Detail.objects.filter(sub_category=id)
    print(worker)
    return render(request, 'main/worker.html', {'result': data, 'worker': worker}, )


def worker_detail(request, id):
    data = website_profile.objects.all()
    worker = User.objects.filter(id=id)
    return render(request, 'main/worker_detail.html', {'result': data, 'worker': worker, }, )


def update_profile(request, id):
    user = User.objects.get(id=id)

    category = Category.objects.filter().order_by('-created')
    subcategory = SubCategory.objects.filter().order_by('-created')
    data = website_profile.objects.all()
    return render(request, 'main/update_profile.html', {'result': data, 'data': user, 'category': category, 'subcategory': subcategory}, )


def update_profile_update(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        workerdata = User_Detail()
        workerdata.user_id = user
        workerdata.category = request.POST['category']
        workerdata.sub_category = request.POST['subcategory']
        print(request.POST['category'], request.POST['subcategory'])
        workerdata.name = request.POST['name']
        workerdata.email = request.POST['email']
        workerdata.dob = request.POST['dob']
        workerdata.area = request.POST['area']
        workerdata.city = request.POST['city']
        workerdata.district = request.POST['district']
        workerdata.zip = request.POST['zip']
        workerdata.state = request.POST['state']
        workerdata.country = request.POST['country']
        workerdata.mobile = request.POST['mobile']
        workerdata.charges = request.POST['rate']
        workerdata.experiance = request.POST['exp']
        workerdata.bio = request.POST['bio']
        workerdata.discription = request.POST['desc']
        workerdata.image = request.FILES['image']

        workerdata.save()
        messages.success(request, 'Data Updated...')
        return redirect('index')

    else:
        return redirect('update_profile')
