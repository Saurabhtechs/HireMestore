# from unicodedata import category
from .models import *
# Create your views here.
from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User
from django.http import JsonResponse
from .filters import CategoryFilter
from django.core.paginator import Paginator
import datetime


def Global_Data(request):
    city = Cities.objects.filter()[:4]
    category = Category.objects.filter().order_by('-created')[:8]
    total_category = Category.objects.count()
    total_user = User.objects.count()
    total_Worker = User_Detail.objects.count()
    total_vistitor = User_Detail.objects.count()
    return {'headcity': city,
            'headcategory': category,
            'total_category': total_category,
            'total_user': total_user,
            'total_Worker': total_Worker,
            'total_vistitor': total_Worker
            }


def index(request):
    digital = Category.objects.filter(type=1).order_by('-created')[:8]
    data = list(digital)
    print(data)
    d = []
    for i in data:
        print(i)
        subcategory = SubCategory.objects.filter(cat=i).count()
        print(subcategory)
        d.append(subcategory)
    print(d)
    helper = Category.objects.filter(type=2).order_by('-created')[:4]
    category = Category.objects.filter().order_by('-created')[:8]
    data0 = SubCategory.objects.filter().order_by('-created')
    # subcategory = SubCategory.objects.filter(cat=data[0]).subcategory.count()
    # subcategory= SubCategory.objects.filter(cat=i).annotate(count=Count('id')).order_by('id')
    # print(subcategory)
    total_Worker = User_Detail.objects.filter(category=5).count()
    data = website_profile.objects.all()
    testimonial = Testimonails.objects.all()
    user = User_Detail.objects.all()
    category_Filter = CategoryFilter(request.GET, queryset=user)

    content = {'result': data, 'testimonial': testimonial, 'category': category,
               'subcategory': d, 'digital': digital, 'helper': helper, 'data0': data0, 'category_filter': category_Filter}
    return render(request, 'frontend/index.html', content)


def SearchCategory(request):
    user = User_Detail.objects.all()
    category_Filter = CategoryFilter(request.GET, queryset=user)
    return render(request, 'frontend/searchcategory.html', {'category_filter': category_Filter})


def Browsebylocation(request):  # type: ignore
    city = Cities.objects.all()[:8]
    return render(request, 'frontend/browse-jobs-location.html', {'city': city})


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

        messages.info(request, 'Message is send')
        return redirect('contact')

    data = website_profile.objects.all()
    return render(request, 'frontend/contact.html', {'result': data},)


def about(request):
    data = website_profile.objects.all()
    return render(request, 'frontend/about.html', {'result': data}, )


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

    cate = list(subcategory)
    get = cate[0]
    worker = User_Detail.objects.filter(sub_category=get)
    return render(request, 'frontend/helper.html', {'result': data, 'worker': worker}, )


def worker_detail(request, id):
    data = website_profile.objects.all()
    worker = User_Detail.objects.get(slug=id)
    worker_gallery = User_Gallery.objects.filter(user=worker)
    return render(request, 'frontend/helper-detail.html', {'result': data, 'worker': worker, 'worker_gallery': worker_gallery}, )


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
        if request.POST['category']:
            category = Category.objects.get(id=request.POST['category'])
        else:
            category = Category.objects.filter(
                id=request.POST['category']).first()
        worker_data.category = category
        if request.POST['Subcategory']:
            subcategory = SubCategory.objects.get(
                id=request.POST['Subcategory'])
        else:
            subcategory = SubCategory.objects.filter(
                id=request.POST['Subcategory']).first()

        worker_data.sub_category = subcategory
        worker_data.name = request.POST['name']
        worker_data.email = request.POST['email']
        worker_data.gender = request.POST['gender']
        # lang = []
        # for i in request.POST.getlist('lang'):
        #     lang.append(i)
        worker_data.lang = request.POST.getlist('lang')
        # worker_data.skill = request.POST['skill']
        dob = datetime.datetime.strptime(
            request.POST['dob'], "%d/%m/%Y").strftime("%Y-%m-%d")
        worker_data.dob = dob  # type: ignore
        city = Cities.objects.get(id=request.POST['city'])
        worker_data.city = city.name
        district = Cities.objects.get(id=request.POST['district'])
        worker_data.district = district.name
        # worker_data.zip = request.POST['zip']
        state = States.objects.filter(id=request.POST['state']).first()
        worker_data.state = state.name  # type: ignore
        country = Country.objects.filter(id=request.POST['country']).first()
        worker_data.country = country.name  # type: ignore
        worker_data.phone = request.POST['phone']
        worker_data.charges = request.POST['charges']
        worker_data.skill = request.POST['availability']
        worker_data.experiance = request.POST['exp']
        worker_data.bio = request.POST['headline']
        worker_data.link = request.POST['link']  # type: ignore
        worker_data.fb = request.POST['fb']  # type: ignore
        worker_data.insta = request.POST['insta']  # type: ignore
        worker_data.google = request.POST['google']  # type: ignore
        worker_data.yt = request.POST['yt']  # type: ignore
        worker_data.website = request.POST['website']  # type: ignore
        worker_data.discription = request.POST['discription']
        if request.FILES.get('imazge'):
            worker_data.image = request.FILES.get('image')
        worker_data.save()

        print(worker_data)
        for gallery in request.FILES.getlist('gallery'):
            gallery_data = User_Gallery.objects.create(
                user=worker_data, gallery=gallery)
            gallery_data.save()
        messages.success(request, 'Data Updated...')
        return redirect('index')

    else:
        return redirect('update_profile')


def Helper_DashBoard(request):
    data = User_Detail.objects.filter(slug='saurabh-soni').first()
    return render(request, 'frontend/helper-dashboard.html', {'helper': data})


def GetCategory(request):
    jsondata = Category.objects.filter(
        type=request.GET['type']).values_list('id', 'name')
    return JsonResponse(dict(jsondata))


def GetSubCategory(request):
    # data = SubCategory.objects.filter(category_id=request.GET['id']).values_list('id','name')
    # return render(request, 'frontend/helper-dashboard.html', {'helper': data})
    jsondata = SubCategory.objects.filter(
        cat_id=request.GET['category_id']).values_list('id', 'name')
    return JsonResponse(dict(jsondata))


# ==================================================================================================
#
def Browsebylocations(request):
    city = Cities.objects.all()
    paginator = Paginator(city, 12)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contaxt = {'page_obj': page_obj}
    return render(request, 'frontend/browse-jobs-location.html', contaxt)


def Browsebylocation(request, id):

    city_data = Cities.objects.filter(name=id)
    cat = Cities.objects.filter(name=id).values_list('name', flat=True)
    cate = list(cat)
    get = cate[0]
    worker = User_Detail.objects.filter(
        city=get)[:10]
    context = {'worker': worker, 'city_data': city_data}
    return render(request, 'frontend/worker.html', context)


def Browsebyskill(request):
    digital = Category.objects.filter(type=1).order_by('-created')[:8]
    return render(request, 'frontend/browse-jobs-skill.html', {'digital': digital})


def StateList(request):
    jsondata = States.objects.filter(
        country_id=request.GET['country_id']).values_list('id', 'name')
    return JsonResponse(dict(jsondata))


def CityList(request):
    jsondata = Cities.objects.filter(
        state_id=request.GET['state_id']).values_list('id', 'name')
    return JsonResponse(dict(jsondata))


def Subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        subcrib_add = SubScribers.objects.create(email=email)
        subcrib_add.save()
    return redirect('index')
