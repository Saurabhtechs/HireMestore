from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.apps import apps
website_profile = apps.get_model('core', 'website_profile')

from rest_framework.decorators import api_view
# Create your views here.


def login(request):
    data = website_profile.objects.all()
    return render(request, 'main/login.html', {'result': data},)

# def UserRegistration(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User(username=username,email=email,password=password)
#         user.save()
#         user_role = UserRole()
#         user_role.mobile_number= request.POST['mobile_number']
#         # user_role.role = request.POST['role']
#         user_role.save()
#         return redirect('https://legalguruindia.com')
#     else:
#         return redirect('home')