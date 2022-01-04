from django.db import models
class BloodType(models.Model):
    blood_type=models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.blood_type

# from accounts.models import CustomUser, Doner, Patient, Hospital







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
