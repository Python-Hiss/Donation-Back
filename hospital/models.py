from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class customUser (User):
    website = models.CharField(max_length=256)
    group = models.ForeignKey(Group, related_name="boes2", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'image')