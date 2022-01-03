from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import CustomUser 

class Post(models.Model):
    user = models.ForeignKey(CustomUser,to_field='username',on_delete=CASCADE)
    content = models.TextField()
    blood_type = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self) :
        return self.content


