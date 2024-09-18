from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
class Follows(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="follower",blank=True)
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name="following",blank=True)