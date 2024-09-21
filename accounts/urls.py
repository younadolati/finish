from django.contrib import admin
from django.urls import path
from accounts.views import rooms,detailuser,follow,room


urlpatterns = [
    path('', rooms, name='rooms'),
    path('<str:username>', detailuser, name='detaailuseer'),
    path('<str:username>/follow/<option>', follow, name='follow'),
    path('rooms/<str:roomname>',room, name='room'),

]
