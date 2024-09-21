from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
class Follows(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="follower",blank=True)
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name="following",blank=True)


class Room (models.Model):
    roomname=models.CharField(max_length=30)
    members=models.ManyToManyField(User,related_name="membership")
    room_image=models.ImageField(upload_to='static/img/')
    desc=models.CharField(max_length=90)
    admin=models.OneToOneField(User,on_delete=models.CASCADE,related_name="adminroom")

    def __str__(self):
        return self.roomname

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="message")
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

