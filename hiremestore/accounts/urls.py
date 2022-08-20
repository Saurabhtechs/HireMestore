from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login, name="login"),
    path('logincheck', views.Logincheck, name="logincheck"),
    path('logout', views.Logout, name="logout"),

    path('register', views.Register, name="register"),
    path('register_submit', views.UserRegister, name="register_submit"),

    

    # path('usersubmit',views.UserRegistration,name="usersubmit"),


]
