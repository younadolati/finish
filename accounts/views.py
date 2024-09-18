from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.
from . import models
from django.contrib.auth.models import User
def test (request):
    return render(request,"A.html",context={})


def detailuser(request,username):
    user=User.objects.get(username=username)
    following=models.Follows.objects.filter(following=user)
    follower=models.Follows.objects.filter(follower=user)


    return render(request,"detailuser.html",context={'user':user,'follower':follower.count(),'following':following.count()})

