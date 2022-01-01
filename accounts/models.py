from django.db import models
from django.contrib.auth.models import User,Group
from phone_field import PhoneField
# Create your models here.
class Account(User):
    age = models.IntegerField(null=True)
    blood_type = models.CharField(max_length=10 ,blank=True,null=True)
    chronic_diseases = models.BooleanField(default=False,blank=True,null=True)
    image = models.ImageField(upload_to = 'image',default='../uploads/image/320.png')
    date = models.DateField(blank=True,null=True,default='2022-01-01')
    isAuthenticated = models.BooleanField(default=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    group = models.ForeignKey(Group, related_name="boes", on_delete=models.CASCADE,default=2)
    location = models.CharField(max_length=50,blank=True,null=True)
    donate = models.BooleanField(default=False)

