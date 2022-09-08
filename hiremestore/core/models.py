from distutils.command.upload import upload
from email.policy import default
from django.db import models
from accounts.models import User
from PIL import Image
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.



class website_profile(models.Model):
    logo = models.ImageField(upload_to='img', max_length=250)
    mobile_number = models.CharField(max_length=15)
    website_title = models.CharField(max_length=50)
    website_subtitle = models.CharField(max_length=100)
    background_img = models.ImageField(upload_to='img', max_length=250)
    favicon = models.ImageField(upload_to='img', max_length=250)
    trusted_by = models.FileField(upload_to='img')
    fb_link = models.CharField(max_length=250)
    twitter_link = models.CharField(max_length=250)
    instagram_link = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.website_title

# class PostImage(models.Model):
#     post = models.ForeignKey(website_profile, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'images/')
 
#     def __str__(self):
#         return self.post.title




class Category(models.Model):
    image = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30 ,unique=True)
    title = models.CharField(max_length=50)
    type = models.IntegerField(default=1)
    feature = models.IntegerField(default=1)
    # slug = models.SlugField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         # Newly created object, so set slug
    #         self.slug = slugify(self.name)

    #         super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img', max_length=250)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    feature = models.IntegerField(default=1)
    # slug = models.SlugField()
    slug = AutoSlugField(populate_from='name')
    created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         # Newly created object, so set slug
    #         self.slug = slugify(self.name)

    #         super(SubCategory, self).save(*args, **kwargs)


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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    charges = models.CharField(max_length=30)
    image = models.ImageField(upload_to='img',null=True)
    bio = models.TextField()
    discription = models.TextField()
    message = models.TextField()
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Country(models.Model):
    sortname= models.CharField(max_length=100)
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "tbl_countries"

class States(models.Model):
    name= models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = "tbl_states"
   

class Cities(models.Model):
    name= models.CharField(max_length=100)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_cities"
   