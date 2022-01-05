from accounts.models import CustomUser, Doner, Patient, Hospital
from django.db import models
class Post(models.Model):
    patient = models.ForeignKey(CustomUser,to_field='username',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self) :
        return f"{self.patient} {self.title}"


class Donation(models.Model):
    doner = models.ForeignKey(Doner,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    notes = models.TextField()
    available = models.BooleanField()

