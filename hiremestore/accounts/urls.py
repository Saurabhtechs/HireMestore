from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login, name="login"),
    path('logincheck', views.Logincheck, name="logincheck"),
    path('logout', views.Logout, name="logout"),

    path('register', views.UserRegister, name="register"),

    path('otp', views.otp, name="otp"),


    

    # path('usersubmit',views.UserRegistration,name="usersubmit"),


]
