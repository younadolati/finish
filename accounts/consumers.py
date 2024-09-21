import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async
from django.contrib.auth.models import User
from accounts.models import Message,Room

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['roomname']
        self.room_group_name=self.room_name
        # Category.objects.create(category=self.channel_name)

        await self.channel_layer.group_add(
            self.room_group_name,self.channel_name
        )
        await self.accept()
        # async_to_sync(self.send(json.dumps({'type':'connection_established',
        #                                 'message':'hellos',
        #                                 })))


    
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message=text_data_json["message"]
        roomname=text_data_json["roomname"]
        username=text_data_json["username"]
        await self.save(
            username,roomname,message
        )
        await self.channel_layer.group_send(
            self.room_group_name , {
            'type':'chat.message',
            'message':message,
            'roomname':roomname,
            'username':username,
        }
        ) 
        # async_to_sync(self.send(text_data=json.dumps({'type':'chat','message':message+"lo"})))


        


    async def chat_message(self, event):
        message=event["message"]
        username=event["username"]
        roomname=event["roomname"]

        await self.send(text_data=json.dumps({'type':'connection_established','message':message,'username':username,'roomname':roomname}))
    
    @sync_to_async
    def save(self,username,roomname,message):
        user=User.objects.get(username=username)
        room=Room.objects.get(roomname=roomname)
        Message.objects.create(user=user,room=room,message=message)

