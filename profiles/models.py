from pickle import TRUE
from statistics import mode
from django.db import models
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    Gender = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(choices=Gender, max_length=2)
    Bio = RichTextField()
    cv = RichTextField()

    def __str__():
        return self.user.username

class Ref_Marital_Status(models.Model):
    MARITAL_STATUS = [
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
    ]
    user = models.ForeignKey(Member, on_delete= models.CASCADE)
    marital_Status_Code = models.CharField(unique=True, blank= TRUE, max_length=50)
    marital_status = models.CharField(choices=MARITAL_STATUS, max_length=20)


class Address(models.Model):
    country = CountryField()
    Zip = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return self.country

class Group(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)
    group_description = RichTextField()
    group_started = models.DateField(auto_now_add=True)
    group_ended = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.group_name

