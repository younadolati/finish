from django.contrib import admin
from django.urls import path
from accounts.views import test,detailuser


urlpatterns = [
    path('', test, name='test'),
    path('<str:username>', detailuser, name='detaailuseer'),

]
