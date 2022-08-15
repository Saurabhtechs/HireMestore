from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index,name="home"),
    # path('usersubmit',views.UserRegistration,name="usersubmit"),


]
