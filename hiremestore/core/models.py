from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.


class website_profile(models.Model):
    logo = models.ImageField(upload_to='img', max_length=250)
    mobile_number = models.CharField(max_length=15)
    website_title = models.CharField(max_length=50)
    website_subtitle = models.CharField(max_length=100)
    background_img = models.ImageField(upload_to='img', max_length=250)
    favicon = models.ImageField(upload_to='img', max_length=250)
    trusted_by = models.ImageField(upload_to='img', max_length=250)
    fb_link = models.CharField(max_length=250)
    twitter_link = models.CharField(max_length=250)
    instagram_link = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website_title

class Category(models.Model):
    image = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    type = models.IntegerField()
    feature = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class SubCategory(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    feature = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Testimonails(models.Model):
    profile = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=50)
    review = models.CharField(max_length=200)


    def __str__(self):
        return self.name
