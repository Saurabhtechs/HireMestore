from django.urls import path
from . import views

urlpatterns = [


#User Login Panel ............................................................................. Start..
    path('login/', views.Login, name="login"),
    path('logincheck', views.Logincheck, name="logincheck"),  # type: ignore
    path('logout', views.Logout, name="logout"),

    path('register', views.UserRegister, name="register"),

    path('otp', views.otp, name="otp"),

#User Login Panel ............................................................................. END..

    

    # path('usersubmit',views.UserRegistration,name="usersubmit"),


]
