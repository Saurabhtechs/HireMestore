from django.contrib import admin
from .models import website_profile, Testimonails, Category, SubCategory
# Register your models here.


admin.site.register(website_profile)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Testimonails)