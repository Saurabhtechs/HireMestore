from django.urls import path,re_path

from . import views

urlpatterns = [

    path('', views.Coreindex, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

    # The home page
    # path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]





