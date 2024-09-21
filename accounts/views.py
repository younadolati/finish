from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models
from django.contrib.auth.models import User
from django.db import transaction

@login_required
def rooms (request):
    rooms=models.Room.objects.all()
    return render(request,"rooms.html",context={'rooms':rooms})

@login_required
def room(request,roomname):
    room=models.Room.objects.get(roomname=roomname)
    messages=models.Message.objects.filter(room=room)[0:25]

    return render(request,"room.html",context={'room':room,'members':room.members.count(),'messages':messages})


def detailuser(request,username):
    user=User.objects.get(username=username)
    following=models.Follows.objects.filter(following=user)
    follower=models.Follows.objects.filter(follower=user)
    follow_status=models.Follows.objects.filter(following=user,follower=request.user).exists()


    return render(request,"detailuser.html",context={'user':user,'follower':follower.count(),'following':following.count(),'follow_status':follow_status})

def follow(request,username,option):
    user=request.user
    following=get_object_or_404(User,username=username)
    try:
        f, created=models.Follows.objects.get_or_create(follower=user,following=following)
        if int(option) == 0:
            f.delete()
            return HttpResponseRedirect(reverse('detaailuseer' ,args=[username]))
        else:
            f.save()
            return HttpResponseRedirect(reverse('detaailuseer' ,args=[username]))


        
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('detaailuseer' ,args=[username]))
        
    

