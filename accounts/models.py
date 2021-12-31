from django.db import models
from django.contrib.auth.models import User,Group
from phone_field import PhoneField
# Create your models here.
class Account(User):
    age = models.IntegerField(null=True)
    blood_type = models.CharField(max_length=10 ,blank=True,null=True)
    chronic_diseases = models.BooleanField(default=False,blank=True,null=True)
    image = models.ImageField(upload_to = 'image')
    data = models.DateField(blank=True,null=True)
    isAuthenticated = models.BooleanField(default=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    group = models.ForeignKey(Group, related_name="boes", on_delete=models.CASCADE)
    location = models.CharField(max_length=50,blank=True,null=True)
    donate = models.BooleanField(default=False)

    def __str__(self) :
        return self.username

