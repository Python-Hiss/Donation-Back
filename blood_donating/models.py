from django.db import models

class BloodType(models.Model):
    blood_type=models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.blood_type

from accounts.models import CustomUser, Doner, Patient, Hospital
class Donation(models.Model):
    doner = models.ForeignKey(Doner,on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    notes = models.TextField()
    available = models.BooleanField()


class Post(models.Model):
    patient = models.ForeignKey(CustomUser,to_field='username',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    # blood_type = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    publish = models.BooleanField()
    
    def __str__(self) :
        return f"{self.patient} {self.title}"


'''
Donation:
- doner -->fk
- timestamp (DateTimeField)
- notes
- hospital
- available Booleand
- Patient --> FK
Post:
    title
    text
    datetime
    patient
    publish Boolean
'''
