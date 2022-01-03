from django.db import models

# Create your models here.


class Area(models.Model):
    area = models.CharField(max_length=100)
    

    def __str__(self):
        return self.area
class City(models.Model):
    city = models.CharField(max_length=100)
    

    def __str__(self):
        return self.city


class Address(models.Model):
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    direction = models.TextField(blank=True,null=True)
    

    # def __str__(self):
    #     return self.area