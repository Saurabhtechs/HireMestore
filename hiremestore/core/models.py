from django.db import models
from accounts.models import User
from django.template.defaultfilters import slugify
from PIL import Image

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
    type = models.IntegerField(default=1)
    feature = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 60 or img.weight > 60:
    #         output_size = (60, 60)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



    def __str__(self):
        return self.name


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    feature = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 60 or img.weight > 60:
    #         output_size = (60, 60)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


    def __str__(self):
        return self.name




class Testimonails(models.Model):
    profile = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30 , unique=True)
    about = models.CharField(max_length=50)
    review = models.CharField(max_length=200)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.profile.path)
    #
    #     if img.height > 100 or img.weight > 100:
    #         output_size = (100, 100)
    #         img.thumbnail(output_size)
    #         img.save(self.profile.path)

    def __str__(self):
        return self.name





class About(models.Model):
    main_img = models.ImageField(upload_to='img', max_length=250)
    description = models.TextField()
    member_name = models.CharField(max_length=50)
    member_img = models.ImageField(upload_to='img', max_length=250)
    member_skill = models.CharField(max_length=30)
    fb_link = models.CharField(max_length=75)
    twitter_link = models.CharField(max_length=75)
    insta_link = models.CharField(max_length=75)
    email_link = models.CharField(max_length=75)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_name





class Contact(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=75)
    mobile = models.IntegerField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class User_Detail(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    experiance = models.CharField(max_length=30)
    bio = models.TextField()
    discription = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name