from django.db import models
from django.contrib.auth.models import AbstractUser
from Address.models import Address
from blood_donating.models import BloodType
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

class CustomUser(AbstractUser):
    ROLES = (

        ('Doner', 'Doner'),
        ('Hospital', 'Hospital'),
        ("Patient","Patient")

    )
    phone_number = models.CharField(max_length=20,blank=True, help_text='Contact phone number')
    address = models.ForeignKey(Address,on_delete=models.CASCADE,default=1,blank=True,null=True,related_name='tracks')
    image = models.ImageField(upload_to = 'image',default='../uploads/image/profile_p.jpg',blank=True,null=True)
    roles = models.CharField(max_length=50, choices = ROLES, null=True,blank=True)
    def __str__(self):
        return self.username


class Doner(CustomUser):
    blood_type = models.ForeignKey(BloodType,on_delete=models.CASCADE,blank=True,null=True,default=1)
    date_of_birth = models.DateField(blank=True,null=True,default='2022-01-01')
    chronic_diseases = models.BooleanField(default=False,blank=True,null=True)

class Patient(CustomUser):
    blood_type = models.ForeignKey(BloodType,on_delete=models.CASCADE,blank=True,null=True,default=1)
    reason = models.TextField()
    date_of_birth = models.DateField(blank=True,null=True,default='2022-01-01')

class Hospital(CustomUser):
    website = models.CharField(max_length=256 ,blank=True,null=True)









@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
