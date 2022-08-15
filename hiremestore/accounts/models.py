from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

# class UserRole(models.Model):
#     id = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
#     mobile_number = models.CharField(max_length=200)
#     role = models.CharField(max_length=200)

#     def __str__(self):
#         return self.mobile_number


class User(AbstractUser):
    phone_number = models.CharField(max_length=12,unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    role = models.CharField(max_length=200)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
