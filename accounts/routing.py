from django.urls import re_path,path
from .consumers import ChatConsumer

websocket_urlpatterns=[
    path('ws/<str:roomname>/',ChatConsumer.as_asgi())
]