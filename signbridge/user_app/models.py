from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone_no=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    website_link=models.URLField(null=True)
    work_experience=models.IntegerField(default=0)
    stud_name=models.CharField(max_length=100)
    org_name=models.CharField(max_length=100,null=True,blank=True)
    org_type=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=20,default="admin")

