from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.Login, name="login"),
    path('logincheck', views.Logincheck, name="logincheck"),
    path('logout', views.Logout, name="logilogoutncheck"),



    # path('usersubmit',views.UserRegistration,name="usersubmit"),


]
