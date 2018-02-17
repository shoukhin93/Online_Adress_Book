from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ContactInfo(models.Model):
    full_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=264)
    date_of_birth = models.CharField(max_length=20)

    def __str__(self):
        return self.nick_name

