from django.urls import path,re_path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
<<<<<<< HEAD
    path('category', views.servies, name='servies'),
    path('worker', views.worker, name='worker'),
    path('worker-detail', views.worker_detail, name='worker_detail'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('update_profile_update/<int:id>',views.update_profile_update,name="update_profile_update"),
=======
    path('servies', views.servies, name='servies'),
>>>>>>> 8daf2258bcd69d864e8428ea2cadcc8d39a1849d


]





