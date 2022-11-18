from django.urls import path,re_path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('enquired_list', views.enquiry, name='enquired_list'),
    path('enquiry_submit', views.enquiry_submit, name='enquiry_submit'),
    path('about', views.about, name='about'),
    path('browsebylocations', views.Browsebylocations, name='browsebylocations'),
    path('browsebylocation/<str:id>', views.Browsebylocation, name='browsebylocation'),

    path('browsebyskill', views.Browsebyskill, name='browsebyskill'),
    path('helper_dashBoard', views.Helper_DashBoard, name='helper_dashBoard'),
    path('get-category', views.GetCategory, name='getcategory'),
    path('get-sub-category', views.GetSubCategory, name='getsubcategory'),

    path('search_category', views.SearchCategory, name='search_category'),

    path('servies', views.servies, name='servies'),
    path('servies/<str:id>', views.subcategory, name='servicesubcategorystr'),
    path('servies/?servies=<str:id>', views.subcategory, name='servicesubcategory'),

    path('worker/<str:id>', views.worker, name='worker'),
    path('worker_detail/<str:id>', views.worker_detail, name='worker_detail'),
    path('update_profile/<str:id>', views.update_profile, name='update_profile'),
    path('update_profile_update/<int:id>', views.update_profile_update,name="update_profile_update"),


    path('statelist', views.StateList, name="statelist"),
    path('citylist',views.CityList, name="citylist"),
    path('subscriber', views.Subscriber, name='subscriber'),





]





