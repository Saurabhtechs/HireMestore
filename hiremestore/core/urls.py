from django.urls import path,re_path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

    path('servies', views.servies, name='servies'),
    path('subcategory/<str:id>', views.subcategory, name='subcategory'),


    path('worker/<str:id>', views.worker, name='worker'),
    path('worker-detail/<int:id>', views.worker_detail, name='worker_detail'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('update_profile_update/<int:id>',views.update_profile_update,name="update_profile_update"),


    path('servies', views.servies, name='servies'),




]





