from django.contrib import admin
from django.urls import path
from accounts.views import test,detailuser,follow


urlpatterns = [
    path('', test, name='test'),
    path('<str:username>', detailuser, name='detaailuseer'),
    path('<str:username>/follow/<option>', follow, name='follow'),


]
