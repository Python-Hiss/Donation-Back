from django.db import models
from django.db.models.base import Model


class BloodType(models.Model):
    blood_type=models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return self.blood_type