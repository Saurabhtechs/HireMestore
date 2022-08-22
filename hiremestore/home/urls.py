# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

# Category Urls End Here......................................................

    path('categorydisplay', views.Categorydisplay,name="categorydisplay"),
    path('category_add',views.CategoryAdd,name="category_add"),
    path('category_save',views.CategorySave,name="category_save"),
    path('category_delete/<int:id>',views.Category_Delete,name="category_delete"),
    path('category_edit/<int:id>',views.CategoryEdit,name="category_edit"),
    path('category_update/<int:id>',views.CategoryUpdate,name="category_update"),

# Category Urls End Here......................................................


# Subcategory Urls Start Here......................................................
    path('subcategorydisplay', views.Subategorydisplay,name="subcategorydisplay"),
    path('subcategory_add',views.SubCategoryAdd,name="subcategory_add"),
    path('subcategory_save',views.SubCategorySave,name="subcategory_save"),
    path('subcategory_delete/<int:id>',views.SubCategory_Delete,name="subcategory_delete"),
    path('subcategory_edit/<int:id>',views.SubCategoryEdit,name="subcategory_edit"),
    path('subcategory_update/<int:id>',views.SubCategoryUpdate,name="subcategory_update"),

# Subcategory Urls End Here......................................................



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
