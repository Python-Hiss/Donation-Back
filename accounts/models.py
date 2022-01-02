from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (

        ('Donater', 'Donater'),
        ('hospital', 'hospital'),
        ("Blood needer","Blood needer")

    )

    date_joined = models.DateField(auto_now_add=True)
    roles = models.CharField(max_length=50, choices = ROLES, null=True,blank=True)
    blood_type = models.CharField(max_length=10 ,blank=True,null=True)
    chronic_diseases = models.BooleanField(default=False,blank=True,null=True)
    image = models.ImageField(upload_to = 'image',default='../uploads/image/320.png')
    date = models.DateField(blank=True,null=True,default='2022-01-01')
    phone_number = models.CharField(max_length=20,blank=True, help_text='Contact phone number')
    location = models.CharField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True,default='2000-01-01')
    website = models.CharField(max_length=256 ,blank=True,null=True)
    def __str__(self):
        return self.username



