from django.urls import path,re_path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
<<<<<<< HEAD
    path('servies', views.servies, name='servies'),
   

    
=======
    path('category', views.servies, name='servies'),
    path('worker', views.worker, name='worker'),
    path('worker-detail', views.worker_detail, name='worker_detail'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('update_profile_update/<int:id>',views.update_profile_update,name="update_profile_update"),
>>>>>>> 1d7f2b5dfd717bb51fbccb2212ec8d5e330daff7


]





